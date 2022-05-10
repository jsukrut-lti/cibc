from django.urls import path
from .views import InsuranceConvoView,PersionalizeCreateView,PersionalizeUpdateView,\
    InsuranceConvoUpdateView,PresentmentUpdateView,PresentmentUpdateViewGBB,\
    InsuranceDiscussionCreate,InsuranceDiscussionList,InsuranceDiscussionGet,\
    InsuranceDiscussionDelete, InsuranceDiscussionUpdate,InsuranceWelcomeView,\
    InsuranceTermConditionView, InsuranceCallback,InsuranceQuestionnaireView,InsuranceApplicantSelectionView,\
    InsuranceCiPreApplicationView, InsuranceClient,InsuranceClientInformationView
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
    path('welcome/<int:pk>', InsuranceWelcomeView.as_view(), name='ins-convo-welcome'),
    path('questionnaire/<int:pk>', InsuranceQuestionnaireView.as_view(), name='ins-convo-questionnaire'),
    path('termCondition/<int:pk>', InsuranceTermConditionView.as_view(), name='ins-convo-tc'),
    path('applicantSelection/<int:pk>', InsuranceApplicantSelectionView.as_view(), name='ins-convo-tc'),
    path('callback/', InsuranceCallback.as_view(), name='ins-callback'),
    path('clientInformation/<int:pk>', InsuranceClientInformationView.as_view(), name='ins-convo-clientInfo'),

]
