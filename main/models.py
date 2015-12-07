from django.db import models
import calendar
# Create your models here.
class Person(models.Model):
    days = [(i, i) for i in range(1,32)]
    months = [(i, calendar.month_name[i]) for i in range(1,13)]
    years = [(i, i) for i in range(2016, 1900, -1)]
    
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    day_of_birth = models.IntegerField(null=True, choices=days)
    month_of_birth = models.IntegerField(null=True, choices=months)
    year_of_birth = models.IntegerField(null=True, choices=years)
    zip_code = models.IntegerField()

    def __unicode__(self):
        return str(self.firstname) + ' ' + str(self.lastname)
