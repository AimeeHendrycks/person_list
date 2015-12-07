from rest_framework import serializers
from main.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('firstname', 'lastname', 'day_of_birth','month_of_birth', 'year_of_birth', 'zip_code')