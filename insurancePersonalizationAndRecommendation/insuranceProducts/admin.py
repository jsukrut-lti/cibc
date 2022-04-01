from django.contrib import admin

# Register your models here.
from .models import InsuranceProduct, InsuranceDiscussion

@admin.register(InsuranceProduct)
class InsuranceProductModelAdmin(admin.ModelAdmin):
    list_display = ['productCode','title','created','modified']


@admin.register(InsuranceDiscussion)
class InsuranceDiscussionModelAdmin(admin.ModelAdmin):
    list_display = ['name','pk','insProduct','agent', 'created', 'modified']

    def name(self, obj):

        return '{} {} age {}'.format(obj.primaryFirstName,obj.primaryLastName,obj.primaryAge)

