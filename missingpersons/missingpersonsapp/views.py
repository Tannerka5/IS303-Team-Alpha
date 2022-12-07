from django.shortcuts import render
from .models import Person
# Create your views here.


def indexPageView(request):
    return render(request, "information/index.html")


def dataPageView(request):
    db_persons = Person.objects.all()

    context = {
        "people": db_persons
    }
    return render(request, "information/data.html", context)


def learnMorePageView(request):
    return render(request, "information/learnmore.html")


def searchPageView(request):

    try:
        first_name = request.GET['first_name']
        people = Person.objects.filter(first_name=first_name)
    except:
        people = Person.object.all()
