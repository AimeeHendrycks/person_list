from django.shortcuts import render, render_to_response
from main.serializers import PersonSerializer
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from rest_framework import generics
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from main.models import Person

def home(request):
    context = {}
    return HttpResponseRedirect('/person_list/')


class APIPersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class APIPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonList(ListView):
    template_name = 'person_list.html'
    paginate_by =20
    def get_queryset(self):
        if 'search' in self.request.GET:
            object_list = Person.objects.filter(lastname__istartswith=self.request.GET['search'])
        else:
            object_list = Person.objects.all()
        print object_list
        return object_list

class PersonDetail(DetailView):
    model = Person
    template_name = 'person_detail.html'

class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    template_name = 'person_create.html'
    success_url = '/person_list/'

class PersonUpdate(UpdateView):
    model = Person
    fields = '__all__'
    template_name = 'person_update.html'
    success_url = '/person_list/'

class PersonDelete(DeleteView):
    model = Person
    template_name = 'person_delete.html'
    success_url = '/person_list/'