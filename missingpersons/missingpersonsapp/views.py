from django.shortcuts import render
from .models import Person
from django.http import HttpResponse
from django.template import loader
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

<<<<<<< HEAD

def searchPageView(request):

    try:
        first_name = request.GET['first_name']
        people = Person.objects.filter(first_name=first_name)
    except:
        people = Person.object.all()

def index(request):
     template = loader.get_template('MyApp/index.html')
     context = {}
     return HttpResponse(template.render(context, request))
=======
def searchPageView(request):
    return render(request, "information/search.html")

def addPersonPageView(request):
    return render(request, "information/add_person.html")
>>>>>>> Tanner_Branch
