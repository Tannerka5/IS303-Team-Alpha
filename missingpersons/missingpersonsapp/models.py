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
        db_table = "missing_persons" #this is important to notice - in pgadmin, the hard coded names and the names you add through the html admin are not stored in the same place, there are 2 different tables