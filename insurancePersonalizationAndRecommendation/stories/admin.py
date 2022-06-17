from django.contrib import admin

# Register your models here.
from .models import *
from django.urls import reverse
from django.utils.html import format_html
from django.conf import settings
from ..accounts.utils import get_user_obj
from django.utils.translation import gettext, gettext_lazy as _

ADDITION = 1
CHANGE = 2
DELETION = 3

ACTION_FLAG_CHOICES = (
    (ADDITION, _('Addition')),
    (CHANGE, _('Change')),
    (DELETION, _('Deletion')),
)

from django.contrib.admin.models import LogEntry
from django.contrib.admin.options import get_content_type_for_model
from django.contrib.admin.utils import flatten_fieldsets

class ModelAdmin(admin.ModelAdmin):


    def log_change(self, request, object, message):
        """
        overriding this method for getting updated content for respective field
        """
        verbose_names = [i['changed']['fields'] for i in message][0]
        for name in verbose_names:
            for field in self.model._meta.fields:
                if name.lower() == str(field.verbose_name).lower():
                    up_content_str = str(getattr(object, field.name))
                    LogEntry.objects.log_action(
                        user_id=request.user.pk,
                        content_type_id=get_content_type_for_model(object).pk,
                        object_id=object.pk,
                        object_repr=up_content_str,
                        action_flag=CHANGE,
                        change_message= 'Changed ' + name,
                    )

    def log_addition(self, request, object, message):
        """
        overriding this method for getting adding content for respective field
        """
        for field in self.model._meta.fields:
            if str(field.verbose_name) not in ['ID', 'created', 'modified','created by','modified by']:

                custom_message = 'Added ' + str(field.verbose_name)
                object_repr = getattr(object, field.name)
                LogEntry.objects.log_action(
                    user_id=request.user.pk,
                    content_type_id=get_content_type_for_model(object).pk,
                    object_id=object.pk,
                    object_repr=str(object_repr),
                    action_flag=ADDITION,
                    change_message=custom_message,
                )

    def get_form(self, request, obj=None, **kwargs):
        objof =str(self).split(".")[1]
        form = super().get_form(request, obj, **kwargs)
        if objof in settings.WORKFLOW_OBJECTS:
            usr_obj = get_user_obj(request.user)
            user_groups = usr_obj.groups.values_list('name',flat = True)
            allowed_groups = settings.ALLOWED_GROUPS
            if obj:
                if allowed_groups.get('maker') in user_groups:
                    form.base_fields['status'].disabled = True
                    if obj.status == 'ap':
                        field_list = list(form.base_fields.keys())
                        for field in field_list:
                            form.base_fields[field].disabled = True
                else:
                    if obj.status == 'ap':
                        field_list = list(form.base_fields.keys())
                        for field in field_list:
                            if field!='status':
                                form.base_fields[field].disabled = True
                if obj.created_by == str(request.user.id):
                    form.base_fields['status'].disabled =True
            else:
                form.base_fields['status'].disabled = True
        return form

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = str(request.user.id)
        obj.modified_by = str(request.user.id)
        obj.save()

@admin.register(Story)
class StoryModelAdmin(ModelAdmin):
    list_display = ['storyName', 'summary', 'created', 'modified']

# # @admin.register(StoryCharacter)
# # class StoryCharactersModelAdmin(ModelAdmin):
# #     list_display = ['story','priorityOrder','character', 'created', 'modified']

@admin.register(StoryStatsTracker)
class StoryStatsTrackersModelAdmin(ModelAdmin):
    list_display = ['story','agent','insuranceDiscussion', 'created', 'modified']

@admin.register(ObjectionHandleStatsTracker)
class ObjectionHandleStatsTrackerModelAdmin(ModelAdmin):
    list_display = ['objectionHandle','agent','insuranceDiscussion', 'created', 'modified']

@admin.register(ObjectioonStatsTracker)
class ObjectioonStatsTrackersModelAdmin(ModelAdmin):
    list_display = ['objection','agent','insuranceDiscussion', 'created', 'modified']


# @admin.register(Objection)
# class StoryCharactersModelAdmin(admin.ModelAdmin):
#     list_display = ['objectionName','primaryIssueOrConcern', 'created', 'modified']

# @admin.register(StoryCharacter)
# class StoryCharactersModelAdmin(ModelAdmin):
#     list_display = ['objectionName','primaryIssueOrConcern', 'created', 'modified', 'get_status']

#     def get_status(self, obj):
#         return obj.my_state_field.label if obj.my_state_field else 0

#     get_status.label = 'status'


@admin.register(ObjectionHandle)
class ObjectionHandleModelAdmin(ModelAdmin):
    list_display = ['buttleName','buttleMessaging','buttleType','objection', 'created', 'modified']

@admin.register(Objection)
class Objection(ModelAdmin):
    list_display = ['objectionName','primaryIssueOrConcern', 'status','created', 'modified']

    # def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
    #     self.change_form_template = 'admin/objection_change_form.html'
    #     return super(ObjectionModelAdmin, self).render_change_form(request, context, add, change, form_url, obj)

