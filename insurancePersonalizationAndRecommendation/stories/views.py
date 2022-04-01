from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from .models import Story,Character
from .forms import StoryForm

class StoryDeleteView(DeleteView):
    model = Story
    form_class = StoryForm
    success_url = reverse_lazy('stories-list')

class StoryView(View):
    form_class = StoryForm
    template_name = 'stories/story_form_template.html'
    context_object_name = 'story_context_object'
    initial = {}


class StoryCreateView(StoryView):
    form_action = '/story/story/create/'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        form.helper.form_action = self.form_action
        return render(request, self.template_name,context= {'storyForm': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect(reverse_lazy('stories-list'))

        form.helper.form_action = self.form_action
        return render(request, self.template_name, {'storyForm': form })

class StoryUpdateView(SingleObjectMixin,StoryView):
    queryset = Story.objects.all()
    form_action = '/story/story/{}/'


    def get(self, request, *args, **kwargs):
        # Look up the object we're interested in.
        self.object = self.get_object()
        form = self.form_class(instance=self.object)
        form.helper.form_action = self.form_action.format(self.object.pk)
        return render(request, self.template_name, {'storyForm': form })

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST,instance=self.object)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect(reverse_lazy('stories-list'))

        form.helper.form_action = self.form_action.format(self.object.pk)
        return render(request, self.template_name, {'storyForm': form })


class StoryListView(ListView):
    model = Story
    def head(self, *args, **kwargs):
        last_story = self.get_queryset().latest('created')
        response = HttpResponse(
            # RFC 1123 date format.
            headers={'Last-Modified': last_story.created.strftime('%a, %d %b %Y %H:%M:%S GMT')},
        )
        return response
