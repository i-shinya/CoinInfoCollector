from django.urls import path

from . import views


urlpatterns = [path("hello/", views.HelloApi.as_view(), name="test-get")]

