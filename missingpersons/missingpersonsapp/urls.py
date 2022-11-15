from django.urls import path
from .views import indexPageView, dataPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("data/", dataPageView, name="data")
]
