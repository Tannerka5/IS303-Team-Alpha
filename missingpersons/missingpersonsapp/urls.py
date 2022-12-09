from django.urls import path
from .views import indexPageView, dataPageView, learnMorePageView, searchPageView, addPersonPageView, searchPersons, addResultPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("data/", dataPageView, name="data"),
    path("learnmore/", learnMorePageView, name="Learn More"),
    path("data/search/", searchPageView, name="Search"),
    path("data/search/search_persons/", searchPersons, name="Search Persons"),
    path("data/add_person/", addPersonPageView, name="Add Person"),
    path("data/add_person/add_result", addResultPageView, name="Add Result")
]
