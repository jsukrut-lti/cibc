from django.shortcuts import render
from .forms import *
from .api import *
from .creditInsurance import *
from .cryptographic import *
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.template.loader import render_to_string
from django.conf import settings
from ..stories.models import Character, Story, StoryCharacter, Objection, ObjectionHandle
from .models import *
from django.views.generic.detail import SingleObjectMixin
import logging
from django.http import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, serializers
from .serializers import InsuranceDiscussionSerializers, InsuranceProductSerializers
from drf_yasg.utils import swagger_auto_schema
import sys
from django.http import HttpResponseRedirect


sys.path.append('../../')
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.http import int_to_base36, base36_to_int


# Get an instance of a logger
logger = logging.getLogger(__name__)


class PersionalizeCreateView(View):
    template_name = 'insurance/personalize.html'
    context_object_name = 'personalize_context_object'

    def get(self, request, *args, **kwargs):
        insDsc = InsuranceDiscussion()
        insDsc.agent = request.user
        insDsc.insProduct = InsuranceProduct.objects.get(productCode="mortgage")
        insDsc.save()
        context = {self.context_object_name: insDsc}
        return render(request, self.template_name, context=context)


class PersionalizeUpdateView(SingleObjectMixin, PersionalizeCreateView):
    queryset = InsuranceDiscussion.objects.all()
    context_object_name = 'personalize_context_object'

    def get(self, request, *args, **kwargs):
        # Look up the object we're interested in.
        self.object = self.get_object()
        context = {self.context_object_name: self.object}
        return render(request, self.template_name, context=context)


class PresentmentUpdateView(PersionalizeUpdateView):
    template_name = 'insurance/personalization_of_gap_and_options/ins_presentment_details.html'
    story_card_template = 'insurance/personalization_of_gap_and_options/storyCard.html'
    concern_card_template = 'insurance/personalization_of_gap_and_options/concernCard.html'

    def getTemplateName(self):
        return self.template_name

    def get(self, request, *args, **kwargs):
        # Look up the object we're interested in.
        self.object = self.get_object()

        if self.object.primaryAge < 30:
            storyName = 'The Young Starter Family'
            primary_objections = ["It costs too much",
                                  "Declined for creditor insurance",
                                  "Reliably pay-off account each month", ]
        elif self.object.primaryAge >= 30 and self.object.primaryAge < 50:
            storyName = 'The Proactive Planner Couple'
            primary_objections = ["It costs too much",
                                  "I already have coverage",
                                  "Reliably pay-off account each month", ]
        else:
            storyName = 'The Recent Retiree'
            primary_objections = ["It costs too much",
                                  "I already have coverage",
                                  "Reliably pay-off account each month", ]

        story_card = self.renderStoryCard(request, storyName)
        concern_card = self.renderConcernCard(request, primary_objections)
        context = {self.context_object_name: self.object,
                   'story_card': story_card,
                   'concern_card': concern_card}
        return render(request, self.getTemplateName(), context=context)

    def renderStoryCard(self, request, storyName):
        story = Story.objects.get(storyName=storyName)
        storyCharacters = StoryCharacter.objects.get(story=story)

        card = render_to_string(self.story_card_template, {
            'img_url': storyCharacters.character.get_character_img_url(),
            'storyName': story.storyName,
            'summary': story.summary,
            'introduction': story.introduction,
            'middle': story.middle,
            'conclusion': story.conclusion,
            'keyInsights': story.keyInsights, })
        return card

    def renderConcernCard(self, request, objectionNames):
        objectionsAndHandlers = []
        for objName in objectionNames:
            objection = Objection.objects.get(objectionName=objName)
            objectionHandlers = ObjectionHandle.objects.filter(objection=objection).all()
            objectionAndHandlers = {'objection': objection, 'objectionHandlers': objectionHandlers, }
            objectionsAndHandlers.append(objectionAndHandlers)

        concern_card = render_to_string(self.concern_card_template, {'objectionsAndHandlers': objectionsAndHandlers})
        return concern_card


class PresentmentUpdateViewGBB(PresentmentUpdateView):
    template_name = 'insurance/personalization_of_gap_and_options/ins_presentment_details_GBB.html'

    def getTemplateName(self):
        return self.template_name

class InsuranceConvoView(View):
    context = {'title': _("Insurance Conversation")}
    template_name = 'insurance/insuranceConversationSingleSheet.html'
    story_card_template = 'insurance/storyCard.html'
    concern_card_template = 'insurance/concernCard3.html'
    article_template = 'insurance/articleSingleSheet.html'

    primary_objections = ["Reliably pay-off account each month", "Talking with spouse/partner"]

    #   "The Recent Retiree"
    def renderStoryCard(self, request, article_id, storyName):
        story = Story.objects.get(storyName=storyName)
        storyCharacters = StoryCharacter.objects.get(story=story)

        card = render_to_string(self.story_card_template, {
            'img_url': storyCharacters.character.get_character_img_url(),
            'storyName': story.storyName,
            'summary': story.summary,
            'introduction': story.introduction,
            'middle': story.middle,
            'conclusion': story.conclusion,
            'keyInsights': story.keyInsights, })
        return card

    def renderConcernCard(self, request, article_id, objectionNames):
        objectionsAndHandlers = []
        for objName in objectionNames:
            objection = Objection.objects.get(objectionName=objName)
            objectionHandlers = ObjectionHandle.objects.filter(objection=objection).all()
            objectionAndHandlers = {'objection': objection, 'objectionHandlers': objectionHandlers, }
            objectionsAndHandlers.append(objectionAndHandlers)

        #        for objHndlrs in objectionsAndHandlers:
        #            for key,value in objHndlrs:

        #           print(objection.objectionName)
        #           print(objection.primaryIssueOrConcern)
        #            for oh in objectionHandlers:
        #                print('\t buttle:{}'.format(oh.buttleMessaging))

        # story = Story.objects.get(storyName=storyName)
        # storyCharacters = StoryCharacter.objects.get(story=story)

        concern_card = render_to_string(self.concern_card_template, {'objectionsAndHandlers': objectionsAndHandlers})
        return concern_card

    def renderArticle(self, request, article_id, form, form_title, form_text, storyName=None, objections=None):
        story_card = ""
        if storyName != None:
            story_card = self.renderStoryCard(request, article_id, storyName)

        concern_card = ""
        if objections != None:
            concern_card = self.renderConcernCard(request, article_id, objections)

        article = render_to_string(self.article_template,
                                   {'id': article_id,
                                    'form_title': form_title,
                                    'form_text': form_text,
                                    'form': form,
                                    'story_card': story_card,
                                    'concern_card': concern_card,
                                    }, request=request)

        return article

    def getImpl(self, request, instance=None):

        if instance == None:
            instance = InsuranceDiscussion()
            instance.agent = request.user
            instance.insProduct = InsuranceProduct.objects.get(productCode="mortgage")
            instance.save()

        self.context['InsuranceDiscussion'] = instance

        # Borrower Info Articles
        primary = self.renderArticle(request,
                                     INS_SHEET_SECTION_AREAS.primary.value,
                                     PrimaryInsuranceDiscussionForm(instance=instance),
                                     _("Primary"),
                                     _("Primary Information"),
                                     "The Young Starter Family",
                                     self.primary_objections)

        co_borrow = self.renderArticle(request,
                                       INS_SHEET_SECTION_AREAS.co_borrow.value,
                                       CoBorrowerInsuranceDiscussionForm(instance=instance),
                                       _("Co-Borrower"),
                                       _("Co-Borrower Information"))

        loved_ones = self.renderArticle(request,
                                        INS_SHEET_SECTION_AREAS.loved_ones.value,
                                        LovedOnesInsuranceDiscussionForm(instance=instance),
                                        _("Financial Dependent Loved Ones"),
                                        _("Loved ones who depend on your income"))

        self.context['borrower_articles'] = [primary, co_borrow, loved_ones]

        self.context['insurance_articles'] = []

        # Financial Articles
        creditProduct = self.renderArticle(request,
                                           INS_SHEET_SECTION_AREAS.creditProduct.value,
                                           CreditProductInsuranceDiscussionForm(instance=instance),
                                           _("Mortgage Info"),
                                           _("Credit product information"))

        incomeExpenseSavingsTotals = self.renderArticle(request,
                                                        INS_SHEET_SECTION_AREAS.incomeExpenseSavingsTotals.value,
                                                        IncomeExpenseSvgTotalsInsuranceDiscussionForm(
                                                            instance=instance),
                                                        _("Income Expenses and Savings Totals"),
                                                        _(""))

        expenseEstimation = self.renderArticle(request,
                                               INS_SHEET_SECTION_AREAS.expenseEstimation.value,
                                               ExpensesEstInsuranceDiscussionForm(instance=instance),
                                               _("Expense Estimation"),
                                               _(""))

        savingsEstimation = self.renderArticle(request,
                                               INS_SHEET_SECTION_AREAS.savingsEstimation.value,
                                               SavingsEstOnesInsuranceDiscussionForm(instance=instance),
                                               _("Savings Estimation"),
                                               _(""))

        self.context['financial_articles'] = [creditProduct, incomeExpenseSavingsTotals, expenseEstimation,
                                              savingsEstimation]

        otherInsurance = self.renderArticle(request,
                                            INS_SHEET_SECTION_AREAS.otherInsurance.value,
                                            OtherInsuranceInsuranceDiscussionForm(instance=instance),
                                            _("Other Insurance"),
                                            _("Other Insurance"))

        self.context['insurance_articles'] = [otherInsurance]

        return render(request, template_name=self.template_name, context=self.context)

    def get(self, request, *args, **kwargs):
        return self.getImpl(request)

    def post(self, request, *args, **kwargs):
        print(request.user.id)
        return render(request, template_name=self.template_name, context=self.context)
        # return self.getImpl(request)


class InsuranceConvoUpdateView(SingleObjectMixin, InsuranceConvoView):
    queryset = InsuranceDiscussion.objects.all()

    def get(self, request, *args, **kwargs):
        # Look up the object we're interested in.

        print(request)
        print(args,kwargs)

        self.object = self.get_object()
        return super().getImpl(request, instance=self.object)

    def str_to_class(self,classname):
        return getattr(sys.modules[__name__], classname)

    def post(self, request, *args, **kwargs):

        submit_from = request.POST.get("submit").split()[1]
        fields = []

        if submit_from == "Personalize":
            fields = ["primaryFirstName","primaryLastName","primaryAge","primaryGender","coFirstName","coLastName","coAge","coGender"]
        else:
            form_dict = {'primary':'PrimaryInsuranceDiscussionForm','co_borrow':'CoBorrowerInsuranceDiscussionForm',
                        'loved_ones':'LovedOnesInsuranceDiscussionForm','creditProduct':'CreditProductInsuranceDiscussionForm',
                        'incomeExpenseSavingsTotals':'IncomeExpenseSvgTotalsInsuranceDiscussionForm',
                        'expenseEstimation':'ExpensesEstInsuranceDiscussionForm',
                        'savingsEstimation':'SavingsEstOnesInsuranceDiscussionForm',
                        'otherInsurance':'OtherInsuranceInsuranceDiscussionForm'}

            formfield_val = form_dict[submit_from]

            class_name = self.str_to_class(formfield_val)

            fields = class_name.Meta.fields

        parent_data = {}
        for col in fields:
            parent_data[col] = request.POST.get(col,False)

        insuranceUpdate = InsuranceDiscussion.objects.filter(pk=int(kwargs.get("pk"))).update(**parent_data)

        queryset = InsuranceDiscussion.objects.all()
        self.object = self.get_object()
        return super().getImpl(request, instance=self.object)


@method_decorator(login_required, name='dispatch')
class InsuranceCiPreApplicationView(View):

    def get(self, request, *args, **kwargs): 
        eligibility_check_instance = InsuranceEligibilityCheckView()
        return eligibility_check_instance.get(request)


@method_decorator(login_required, name='dispatch')
class InsuranceNonEligibleView(View):

    def __init__(self):
        self.template_name = 'creditInsurance/notEligible.html'
        self.context_object_name = 'Not Eligible'


    def get_template(self, request, *args, **kwargs):

        content_rec = InsuranceNonEligibleContent.objects.filter(effective_start_date__lte=datetime.datetime.now().date(),
                                                                     effective_end_date__gte=datetime.datetime.now().date(),
                                                                     active=True).values('content')
        content_rec = content_rec and list(content_rec) or []
        if content_rec:
            occupation_rec = content_rec and content_rec[0] or {}
            content = occupation_rec.get('content', False)

        context = {'menu_name': self.context_object_name,'content': content}
        return render(request, template_name=self.template_name, context=context)


@method_decorator(login_required, name='dispatch')
class InsuranceWelcomeView(View):

    def __init__(self):
        self.template_name = 'creditInsurance/welcome.html'
        self.context_object_name = 'Welcome'

    def get_template(self, request, *args, **kwargs):
        pk_id = CrypticSetting.encrypt(self, args[0])
        context = {'menu_name': self.context_object_name, 'pk_id': pk_id}
        return render(request, template_name=self.template_name, context=context)


class InsuranceEligibilityCheckView(object):

    def __init__(self):
        self.insurance_json_data = CreditInsurance.api_data()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            insurance_data = self.insurance_json_data

            # new logic will be build based upon Json Format
            input_data = {}

            input_data['credit_product'] = insurance_data["sourceApplication"]
            input_data['insurance_product_details'] = insurance_data["insProducts_details"]
            input_data['applicants'] = insurance_data["applicants"]

            get_response = True
            eligibility_instance = EligibilityCheck()
            get_response = eligibility_instance.get_eligibility(request,**input_data)

            if get_response == True:            #if eligible

                # json data stored into DB
                pre_data_ID = CreditInsurance.initial_data_storage(**insurance_data)

                return InsuranceWelcomeView().get_template(request,pre_data_ID)
            else:
                return InsuranceNonEligibleView().get_template(request)


@method_decorator(login_required, name='dispatch')
class InsuranceQuestionnaireView(View):
    template_name = 'creditInsurance/questionnaire.html'
    context_object_name = 'Questionnaire'
    assessment_details = {}

    def post(self, request, *args, **kwargs):

        self.assessment_details = AssessmentQuestionnaire.assessment_data(self, request)

        context = {'menu_name': self.context_object_name,'assessment': self.assessment_details,'pk_id': request.POST.get("pk_id")}
        return render(request, template_name=self.template_name, context=context)


@method_decorator(login_required, name='dispatch')
class InsuranceTermConditionView(View):
    template_name = 'creditInsurance/TermsAndConditions.html'
    context_object_name = 'Terms & Condition'

    def post(self, request, *args, **kwargs):

        context = {'menu_name': self.context_object_name,'id' :  request.POST.get("pk_id")}
        return render(request, template_name=self.template_name, context=context)


@method_decorator(login_required, name='dispatch')
class InsuranceApplicantSelectionView(View):
    template_name = 'creditInsurance/applicantSelection.html'
    context_object_name = 'Applicant Selection'

    def get(self, request, *args, **kwargs):

        appl_details_remaining = []
        appl_details_remaining = ApplicantDetails.get_applicant_details(self,**kwargs)

        context = {'menu_name': self.context_object_name, 'applicant_details': appl_details_remaining, 'pk_id': kwargs['pk']}

        return render(request, template_name=self.template_name, context=context)


@method_decorator(login_required, name='dispatch')
class InsuranceApplicantDemographicView(View):

    def post(self, request, *args, **kwargs):
        payload = request.POST
        single_select = payload.getlist('singleSelect')
        multi_select = payload.getlist('multiSelect')
        joint_applicant = payload.get('jointApplicant')
        select = multi_select if joint_applicant == 'Yes' else single_select

        pk = CrypticSetting.decrypt(self, payload.get("pk_id"))
        queryset = InsurancePreProcessData.objects.filter(id=pk).values()[0]
        filter_data, appDetails = CreditInsurance.format_raw_data_for_insdisc(self,queryset, select)

        discussionDetails = InsuranceDiscussion.objects.create(**filter_data)
        discussionDetails.save()

        discussion_appDetails = dict()
        for app_id in appDetails:
            discussion_appDetails['insDiscussion_id'] = discussionDetails.pk
            discussion_appDetails['application_number'] = filter_data['application_number']
            discussion_appDetails['applicantID'] = app_id

            applicantDetails = InsuranceDiscussionApplicantDetails.objects.create(**discussion_appDetails)
            applicantDetails.save()

        discussion_pk = CrypticSetting.encrypt(self, discussionDetails.pk)
        return HttpResponseRedirect('/insurance/clientInformation/{}'.format(discussion_pk))


class InsuranceClientInformationView(View):
    template_name = 'creditInsurance/clientInformation.html'
    context_object_name = 'Client'

    def get(self, request, *args, **kwargs):
        pk = CrypticSetting.decrypt(self, kwargs['pk'])
        queryset = InsuranceDiscussion.objects.filter(id=pk).values()[0]
        if queryset['primaryGender'] == 'm':
            queryset['primaryGender'] = 'Male'
        elif queryset['primaryGender'] == 'f':
            queryset['primaryGender'] = 'Female'
        else:
            queryset['primaryGender'] = 'Other'

        if queryset['canada_provence'] == 'on':
            queryset['canada_provence'] = 'Canada'

        context = {
            'id': kwargs['pk'],
            'discussion': queryset,
            'menu_name': self.context_object_name
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = request.POST.form()
        return render(request, template_name=self.template_name, context=context)


class InsuranceClient(View):
    template_name = 'ci_tool/client.html'

    def get(self, request, *args, **kwargs):
        context = {
            'id': kwargs['pk']
        }
        return render(request, template_name=self.template_name, context=context)


class InsuranceExitApplicationView(View):
    template_name = 'creditInsurance/exitApplication.html'
    context_object_name = 'Exit'

    def get(self, request, *args, **kwargs):
        context = {'menu_name': self.context_object_name}
        return render(request, template_name=self.template_name, context=context)


class InsuranceCallback(View):

    def get(self, request, *args, **kwargs):
        print(kwargs)

    def post(self, request, *args, **kwargs):
        print("request")


class DashbboardView(View):
    template_name = 'creditInsurance/dashboard.html'

    def post(self, request, *args, **kwargs):
        context = {
            'id': request.POST.get("pk_id"),
        }
        return render(request, template_name=self.template_name, context=context)


class InsuranceTermCondition2View(View):
    template_name = 'creditInsurance/TermsAndConditions2.html'

    def get(self, request, *args, **kwargs):
        context = {
            'id': kwargs['pk'],
        }
        return render(request, template_name=self.template_name, context=context)

class SummaryView(View):
    template_name = 'creditInsurance/saveSummary.html'

    def get(self, request, *args, **kwargs):
        context = {
            'id': kwargs['pk'],
        }
        return render(request, template_name=self.template_name, context=context)

class ExitView(View):
    template_name = 'creditInsurance/clientExitSurvey.html'

    def get(self, request, *args, **kwargs):
        context = {
            'id': kwargs['pk'],
        }
        return render(request, template_name=self.template_name, context=context)

class ExitApplication(View):
    template_name = 'creditInsurance/exitApplication.html'

    def get(self, request, *args, **kwargs):
        context = {
            'id': kwargs['pk'],
        }
        return render(request, template_name=self.template_name, context=context)

