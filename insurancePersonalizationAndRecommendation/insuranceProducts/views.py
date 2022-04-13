from django.shortcuts import render
from .forms import *
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.template.loader import render_to_string
from django.conf import settings
from ..stories.models import Character, Story, StoryCharacter, Objection, ObjectionHandle
from .models import InsuranceDiscussion, InsuranceProduct
from django.views.generic.detail import SingleObjectMixin
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, serializers
from .serializers import InsuranceDiscussionSerializers, InsuranceProductSerializers
from drf_yasg.utils import swagger_auto_schema

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
        self.object = self.get_object()
        return super().getImpl(request, instance=self.object)


class InsuranceDiscussionAPI(APIView):
    """
        Retrieve, update or delete a InsuranceDiscussion i.
    """
    def response(self, data=None, success=True, **message):
        if data and success:
            return Response(data={"result": "success", "data": data},
                            status=status.HTTP_200_OK)
        elif success:
            return Response(data={"result": "success"},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "failed", "message": message.get("err", "UNKNOWN ERROR")},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.request.GET['id']:
            insurance_discussions = InsuranceDiscussion.objects.filter(id=request.GET['id']).values()
        else:
            insurance_discussions = InsuranceDiscussion.objects.all().values()
        if insurance_discussions:
            self.response(data=insurance_discussions)
        else:
            self.response(success=False, err='No data found')


    def post(self, request):
        serializer = InsuranceDiscussionSerializers(data=request.data)
        if serializer.is_valid():
            save_rec = serializer.save()
            self.response(data=[{'record_id': save_rec}])
        else:
            self.response(success=False, err=serializer.errors)


    def put(self, request):
        dis = InsuranceDiscussion.objects.get(id=request.GET['id'])
        serializer = InsuranceDiscussionSerializers(instance=dis, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            self.response(data=serializer.validated_data)
        else:
            self.response(success=False, err=serializer.errors)


    def delete(self, request):
        insurance_discussion = InsuranceDiscussion.objects.filter(id=request.GET['id'])
        if insurance_discussion:
            insurance_discussion.delete()
            self.response()
        else:
            self.response(success=False, err="No data found")




class InsuranceDiscussionCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(query_serializer=InsuranceDiscussionSerializers)
    def post(self, request):
        serializer = InsuranceDiscussionSerializers(data=request.data)
        if serializer.is_valid():
            save_rec = serializer.save()
            return Response(data={"result": "success", "record_id": save_rec.id},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "error", "data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class InsuranceDiscussionList(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(query_serializer=InsuranceDiscussionSerializers)
    def get(self, request):
        insurance_discussions = InsuranceDiscussion.objects.all().values()
        serializer = InsuranceDiscussionSerializers(insurance_discussions, many=True)
        if insurance_discussions:
            return Response(data={"result": "success", "data": insurance_discussions},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "No data found"},
                            status=status.HTTP_400_BAD_REQUEST)


class InsuranceDiscussionGet(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(query_serializer=InsuranceDiscussionSerializers)
    def get(self, request):
        insurance_discussion = InsuranceDiscussion.objects.filter(id=request.GET['id']).values()
        serializer = InsuranceDiscussionSerializers(insurance_discussion, many=True)
        if insurance_discussion:
            return Response(data={"result": "success", "data": insurance_discussion},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "No data found"},
                            status=status.HTTP_400_BAD_REQUEST)


class InsuranceDiscussionDelete(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(query_serializer=InsuranceDiscussionSerializers)
    def delete(self, request):
        insurance_discussion = InsuranceDiscussion.objects.filter(id=request.GET['id'])
        if insurance_discussion:
            insurance_discussion.delete()
            return Response(data={"result": "success"},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "No data found"},
                            status=status.HTTP_400_BAD_REQUEST)


class InsuranceDiscussionUpdate(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(query_serializer=InsuranceDiscussionSerializers)
    def put(self, request):
        dis = InsuranceDiscussion.objects.get(id=request.GET['id'])
        serializer = InsuranceDiscussionSerializers(instance=dis, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"result": "success", "data": serializer.validated_data},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"result": "No data found"},
                            status=status.HTTP_400_BAD_REQUEST)
