from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        date_missing = request.POST['date_missing']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        age_at_missing = request.POST['age_at_missing']
        city = request.POST['city']
        state = request.POST['state']
        gender = request.POST['gender']
        race = request.POST['race']

        new_person = Person()
        new_person.date_missing = date_missing
        new_person.last_name = last_name
        new_person.first_name = first_name
        new_person.age_at_missing = age_at_missing
        new_person.city = city
        new_person.state = state
        new_person.gender = gender
        new_person.race = race

        new_person.save()

        return redirect('Add Result')

    return render(request, "information/add_person.html")

def searchPersons(request):
    first_name = request.GET.get('first_name')

    persons = Person.objects.filter(first_name=first_name)

    context = {
        'persons': persons
    }

    return render(request, "information/search_persons.html", context)

def addResultPageView(request):
    return render(request, "information/add_result.html")