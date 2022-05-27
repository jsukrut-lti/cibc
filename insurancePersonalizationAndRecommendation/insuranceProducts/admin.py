from django.contrib import admin
from ..stories.admin import ModelAdmin

# Register your models here.
from .models import InsuranceProduct, InsuranceDiscussion,dumpData

@admin.register(InsuranceProduct)
class InsuranceProductModelAdmin(admin.ModelAdmin):
    list_display = ['productCode','title','created','modified']


@admin.register(InsuranceDiscussion)
class InsuranceDiscussionModelAdmin(ModelAdmin):
    list_display = ['name','pk','insProduct','agent', 'created', 'modified']

    def name(self, obj):

        return '{} {} age {}'.format(obj.primaryFirstName,obj.primaryLastName,obj.primaryAge)

@admin.register(dumpData)
class dumpDataModelAdmin(admin.ModelAdmin):
    list_display = ['status','created','modified']