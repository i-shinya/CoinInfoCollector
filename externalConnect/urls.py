from django.urls import path

from . import views


urlpatterns = [path("external/", views.ExternalApi.as_view(), name="extermal-test")]

