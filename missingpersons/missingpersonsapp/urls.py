from django.urls import path
from .views import indexPageView, dataPageView, learnMorePageView, searchPageView, addPersonPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("data/", dataPageView, name="data"),
    path("learnmore/", learnMorePageView, name="Learn More"),
    path("search/", searchPageView, name="search"),
    path("add_person/", addPersonPageView, name="Add Person")
]
