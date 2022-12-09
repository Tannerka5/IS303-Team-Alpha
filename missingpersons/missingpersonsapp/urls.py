from django.urls import path
<<<<<<<<< Temporary merge branch 1
from .views import indexPageView, dataPageView, learnMorePageView, searchPageView, addPersonPageView
=========
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import indexPageView, dataPageView, learnMorePageView, searchPageView
>>>>>>>>> Temporary merge branch 2

urlpatterns = [
    path("", indexPageView, name="index"),
    path("data/", dataPageView, name="data"),
    path("learnmore/", learnMorePageView, name="Learn More"),
    path("data/search/", searchPageView, name="search"),
    path("data/add_person/", addPersonPageView, name="Add Person")
]

urlpatterns += staticfiles_urlpatterns()