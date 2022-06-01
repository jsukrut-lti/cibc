from django.contrib import admin

# Register your models here.
from .models import *
from django.urls import reverse
from django.utils.html import format_html
from django.conf import settings

@admin.register(Character)
class CharactersModelAdmin(admin.ModelAdmin):
    list_display = ['characterName', 'backstory', 'characterImage','created', 'modified']
    #fields = [Character._meta.get_fields()]

    # change_form_template = 'admin/admin_test_change_form.html'

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        self.change_form_template = 'admin/admin_test_change_form.html'
        context['base_url'] = settings.AVATARS_SERVER_URL
        context['avatar_url'] = obj.get_character_img_url()

        return super(CharactersModelAdmin, self).render_change_form(request, context, add, change, form_url, obj)
l

    def characterImage(self, obj):

        return format_html('<img src="{}" width="150" height="150" >',obj.get_character_img_url())

    characterImage.short_description = "Avatar"

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        #form.base_fields["characterName"].label = "Character Name (Humans only!):"
        #form.base_fields["characterImage"].label = 'Avatar'
        #form.base_fields["avatarImage"]
        return form


@admin.register(Story)
class StoryModelAdmin(admin.ModelAdmin):
    list_display = ['storyName', 'summary', 'created', 'modified']

@admin.register(StoryCharacter)
class StoryCharactersModelAdmin(admin.ModelAdmin):
    list_display = ['story','priorityOrder','character', 'created', 'modified']

@admin.register(StoryStatsTracker)
class StoryCharactersModelAdmin(admin.ModelAdmin):
    list_display = ['story','agent','insuranceDiscussion', 'created', 'modified']

@admin.register(ObjectionHandleStatsTracker)
class StoryCharactersModelAdmin(admin.ModelAdmin):  ```````
    list_display = ['objectionHandle','agent','insuranceDiscussion', 'created', 'modified']

@admin.register(ObjectioonStatsTracker)
class StoryCharactersModelAdmin(admin.ModelAdmin):
    list_display = ['objection','agent','insuranceDiscussion', 'created', 'modified']


@admin.register(Objection)
class StoryCharactersModelAdmin(admin.ModelAdmin):
    list_display = ['objectionName','primaryIssueOrConcern', 'created', 'modified']

@admin.register(ObjectionHandle)
class StoryCharactersModelAdmin(admin.ModelAdmin):
    list_display = ['buttleName','buttleMessaging','buttleType','objection', 'created', 'modified']

