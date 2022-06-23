from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('insConvo/', InsuranceConvoView.as_view(), name='ins-convo'),
    path('insConvo/<int:pk>/', InsuranceConvoUpdateView.as_view(), name='ins-convo-update'),
    path('presentOptions/',TemplateView.as_view(template_name="insurance/personalization_of_gap_and_options/ins_presentment_details.html"),name='ins-options'),
    path('presentOptions/<int:pk>/', PresentmentUpdateView.as_view(), name='ins-options-update'),
    path('presentOptions_GBB/<int:pk>/', PresentmentUpdateViewGBB.as_view(), name='ins-options-update-gbb'),
    path('personalize/<int:pk>/', PersionalizeUpdateView.as_view(), name='personalize-update'),
    path('personalize/', PersionalizeCreateView.as_view(), name='personalize-create'),
    path('ins_dis_create/',InsuranceDiscussionCreate.as_view()),
    path('ins_dis_list/',InsuranceDiscussionList.as_view()),
    path('ins_dis_get/',InsuranceDiscussionGet.as_view()),
    path("ins_dis_del/",InsuranceDiscussionDelete.as_view()),
    path("ins_dis_update/",InsuranceDiscussionUpdate.as_view()),
    path('ci_pre_application/', InsuranceCiPreApplicationView.as_view(), name='ins-convo-ci-pre-application'),
    path('welcome/', InsuranceWelcomeView.as_view(), name='ins-convo-welcome'),
    path('questionnaire/', InsuranceQuestionnaireView.as_view(), name='ins-convo-questionnaire'),
    path('termCondition/', InsuranceTermConditionView.as_view(), name='ins-convo-tc'),
    path('applicantSelection/<str:pk>', InsuranceApplicantSelectionView.as_view(), name='ins-convo-tc'),
    path('applicantDemographic/', InsuranceApplicantDemographicView.as_view(), name='ins-convo-tc'),
    path('callback/', InsuranceCallback.as_view(), name='ins-callback'),
    path('clientInformation/<str:pk>', InsuranceClientInformationView.as_view(), name='ins-convo-clientInfo'),
    path('dashboard/', DashbboardView.as_view(), name='ins-dashboard'),
    path('termCondition2/<int:pk>', InsuranceTermCondition2View.as_view(), name='ins-convo-tc'),
    path('summary/<int:pk>', SummaryView.as_view(), name='ins-summary'),
    path('exit/<int:pk>', ExitView.as_view(), name='ins-exit'),
    path('exitApplication/<int:pk>', ExitApplication.as_view(), name='ins-exit'),
    path('anecdotesArchetypeInformation/<int:pk>', AnecdotesArchetypeInformation.as_view(), name='ins-exit'),
    path('anecdotesArchetypeSelection/<int:pk>', AnecdotesArchetypeSelection.as_view(), name='ins-exit'),
    path('faq/<int:pk>', FAQ.as_view(), name='ins-exit'),

]