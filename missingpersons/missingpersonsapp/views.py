from django.shortcuts import render

# Create your views here.


def indexPageView(request):
    return render(request, "information/index.html")


def dataPageView(request):
    return render(request, "information/data.html")


def learnMorePageView(request):
    return render(request, "information/learnmore.html")
