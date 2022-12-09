from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import indexPageView, dataPageView, learnMorePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("data/", dataPageView, name="data"),
    path("learnmore/", learnMorePageView, name="Learn More"),
]

urlpatterns += staticfiles_urlpatterns()