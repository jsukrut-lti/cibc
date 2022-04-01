from django.urls import path
from .views import StoryListView, StoryCreateView,StoryDeleteView,StoryUpdateView
from django.views.generic import TemplateView

class CharacterAndStoryInventoryView(TemplateView):
    template_name = 'stories/characterAndStoryInventory.html'

class CharacterEditorView(TemplateView):
    template_name = 'stories/characterEditor.html'

class StoryEditorView(TemplateView):
    template_name = 'stories/storyEditor.html'

urlpatterns = [
    path('CharacterAndStoryInventoryView/', CharacterAndStoryInventoryView.as_view(), name='CharacterAndStoryInventoryView'),
    path('CharacterEditorView/', CharacterEditorView.as_view(), name='CharacterEditorView'),
    path('StoryEditorView/', StoryEditorView.as_view(), name='StoryEditorView'),
    path('stories/', StoryListView.as_view(), name='stories-list'),
    #path('storiesDetail/', StoryDetailView.as_view(), name='story-detail-new'),
    #path('storiesDetail/<int:pk>/', StoryDetailView.as_view(), name='story-detail-lookup'),

    path('story/create/', StoryCreateView.as_view(), name='story-create'),
    path('story/<int:pk>/', StoryUpdateView.as_view(), name='story-update'),
    path('story/<int:pk>/delete/', StoryDeleteView.as_view(), name='story-delete'),

]

