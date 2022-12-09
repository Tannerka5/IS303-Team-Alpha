from django.urls import path
from .views import indexPageView, dataPageView, learnMorePageView, searchPageView, addPersonPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("data/", dataPageView, name="data"),
    path("learnmore/", learnMorePageView, name="Learn More"),
    path("data/search/", searchPageView, name="search"),
    path("data/add_person/", addPersonPageView, name="Add Person")
]

urlpatterns += staticfiles_urlpatterns()