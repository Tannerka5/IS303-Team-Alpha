from django.db import models

# Create your models here.


class Person(models.Model):
    date_missing = models.DateField(max_length=45)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    age_at_missing = models.CharField(max_length=3)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    race = models.CharField(max_length=50)

    list_display = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    class Meta:
        db_table = "missing_persons"
