from django.urls import path
from .views import indexPageView, dataPageView, learnMorePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("data/", dataPageView, name="data"),
    path("learnmore/", learnMorePageView, name="Learn More"),
]
