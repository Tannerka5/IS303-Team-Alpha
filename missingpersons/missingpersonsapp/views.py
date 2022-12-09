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
    return render(request, "information/data.html", {'db_persons': db_persons})


def learnMorePageView(request):
    return render(request, "information/learnmore.html")

def searchPageView(request):
    return render(request, "information/search.html")

def addPersonPageView(request):
    return render(request, "information/add_person.html")

def searchPersons(request):
    first_name = request.GET.get('first_name')

    persons = Person.objects.filter(first_name=first_name)

    context = {
        'persons': persons
    }

    return render(request, "information/search_persons.html", context)