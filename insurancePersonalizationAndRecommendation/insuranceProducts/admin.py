from django.contrib import admin
from ..stories.admin import ModelAdmin

# Register your models here.
from .models import InsuranceProduct, InsuranceDiscussion, InsurancePreProcessData, InsuranceEligibility, \
    InsuranceCreditProduct, \
    ProvinceResidence, OccupationMaster, InsuranceNonEligibleContent, ClientDetails, AssessmentQuestionnaireMaster, \
    ExitSurveyMaster


@admin.register(InsuranceProduct)
class InsuranceProductModelAdmin(admin.ModelAdmin):
    list_display = ['productCode','title','creditProduct_code','created','modified']


@admin.register(InsuranceDiscussion)
class InsuranceDiscussionModelAdmin(ModelAdmin):
    list_display = ['name','pk','insProduct','agent', 'created', 'modified']

    def name(self, obj):

        return '{} {} age {}'.format(obj.primaryFirstName,obj.primaryLastName,obj.primaryAge)

@admin.register(InsurancePreProcessData)
class InsurancePreProcessDataModelAdmin(admin.ModelAdmin):
    list_display = ['application_number','status','created','modified']


@admin.register(InsuranceEligibility)
class InsuranceEligibilityModelAdmin(admin.ModelAdmin):
    list_display = ['insProduct','minAge','maxAge','residency','occupation', 'created', 'modified']


@admin.register(InsuranceCreditProduct)
class InsuranceCreditProductModelAdmin(admin.ModelAdmin):
    list_display = ['credit_product_code','credit_product_name','active', 'created', 'modified']


@admin.register(ProvinceResidence)
class ProvinceResidenceModelAdmin(admin.ModelAdmin):
    list_display = ['province','description','residency','active', 'created', 'modified']


@admin.register(OccupationMaster)
class OccupationMasterModelAdmin(admin.ModelAdmin):
    list_display = ['occupation_code', 'occupation_name', 'active', 'created', 'modified']


@admin.register(InsuranceNonEligibleContent)
class InsuranceNonEligibleContentModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'effective_start_date','effective_end_date', 'active', 'created', 'modified']


@admin.register(AssessmentQuestionnaireMaster)
class AssessmentQuestionnaireMasterModelAdmin(admin.ModelAdmin):
    list_display = ['assessment_id', 'assessment_details','effective_start_date','effective_end_date', 'active', 'created', 'modified']


@admin.register(ExitSurveyMaster)
class ExitSurveyMasterModelAdmin(admin.ModelAdmin):
    list_filter = ['exit_id', 'exit_selector', 'exit_radio_disply', 'exit_msg_line0', 'exit_msg_line1', 'exit_msg_line2']
