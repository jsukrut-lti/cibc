"""insurancePersonalizationAndRecommendation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.views.generic import TemplateView, RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
   openapi.Info(
      title="CIBC API",
      default_version='v1',
      description="Test description",
      terms_of_service="127.0.0.1:8000",
      contact=openapi.Contact(email="test@test.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin_base.html'), name='login'),
    path('admin/', admin.site.urls),  # admin site
    path('', RedirectView.as_view(url='/auth/login/')),
    path('auth/', include('django.contrib.auth.urls')),  # home
    path('account/', include('insurancePersonalizationAndRecommendation.accounts.urls')),  # home
    path('insurance/', include('insurancePersonalizationAndRecommendation.insuranceProducts.urls')), # home
    path('story/', include('insurancePersonalizationAndRecommendation.stories.urls')),
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('compass_start/', TemplateView.as_view(template_name="compass_start.html"), name='compass_start'),
    path('mortgage_product/', TemplateView.as_view(template_name="mortgage_product/mortgage.html"), name='mortgage'),
    path('insurance_api/',include('insurancePersonalizationAndRecommendation.insuranceProducts.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('oauth2/', include('django_auth_adfs.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),