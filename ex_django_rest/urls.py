"""ex_django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'question', views.QuestionViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls, namespace='api')),

    # Add static file serving for DEBUG
    url(r'^', include('django.contrib.staticfiles.urls')),
]
