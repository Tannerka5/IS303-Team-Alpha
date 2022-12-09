from django.db import models

# Create your models here.


class Person(models.Model):
    date_missing = models.DateField(max_length=45)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    age_at_missing = models.IntegerField
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    race = models.CharField(max_length=50)

    def __str__(self):
        return self.city

    class Meta:
        db_table = "person" #this was an issue, the persons that we hard coded and the people we add through admin were saving to 2 different tables in the db. I changed this from missing_persons to just person so it would all be compiled in the same spot ZE
