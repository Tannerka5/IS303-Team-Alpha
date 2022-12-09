from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import indexPageView, dataPageView, learnMorePageView, searchPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("data/", dataPageView, name="data"),
    path("learnmore/", learnMorePageView, name="Learn More"),
    path("search/", searchPageView, name="search")
]

urlpatterns += staticfiles_urlpatterns()