from django.urls import path
from .views import InsuranceConvoView,PersionalizeCreateView,PersionalizeUpdateView,\
    InsuranceConvoUpdateView,PresentmentUpdateView,PresentmentUpdateViewGBB,\
    InsuranceDiscussionCreate,InsuranceDiscussionList,InsuranceDiscussionGet,\
    InsuranceDiscussionDelete
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
    path("ins_dis_del/",InsuranceDiscussionDelete.as_view())
]
