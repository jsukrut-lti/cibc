from django.forms import ModelForm,Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from .models import Story, Character

class StoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()

        # Setup Helper Info
        self.helper.form_id = 'id-storiesDetail'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        #self.helper.form_action = '/story/story/save/'
        self.helper.add_input(Submit('submit', 'Submit Story', css_class='btn-primary'))

        super(StoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Story
        #fields = ['storyName', 'summary', 'introduction', 'middle', 'conclusion', 'keyInsights']
        fields = '__all__'
        widgets = {
            'summary': Textarea(attrs={'cols': 50, 'rows': 6}),
            'introduction': Textarea(attrs={'cols': 50, 'rows': 6}),
            'middle': Textarea(attrs={'cols': 50, 'rows': 6}),
            'conclusion': Textarea(attrs={'cols': 50, 'rows': 6}),
            'keyInsights': Textarea(attrs={'cols': 50, 'rows': 6}),
        }










