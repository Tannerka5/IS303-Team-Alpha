# Generated by Django 4.1.2 on 2022-12-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missingpersonsapp', '0002_person_age_at_missing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age_at_missing',
            field=models.CharField(max_length=3),
        ),
    ]
