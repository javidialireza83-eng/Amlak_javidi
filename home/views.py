from django.shortcuts import render
from .models import Home
from .forms import HomeForms
from .seriailzers import HomeSeriailzer
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

class List_View(generic.ListView):
    model=Home
    template_name='home/post_list.html'
    context_object_name='posts'
    
class Detail_View(generic.DetailView):
    model=Home
    template_name='home/post_detail.html'
    context_object_name='post'

class Create_View(LoginRequiredMixin,generic.CreateView):
    model=Home
    form_class=HomeForms
    template_name='home/post_create.html'
    success_url=reverse_lazy('list')
    
class Update_View(LoginRequiredMixin,generic.UpdateView):
    model=Home
    # fields='__all__'
    form_class=HomeForms
    template_name='home/post_update.html'
    success_url=reverse_lazy('list')
    
class Detele_View(LoginRequiredMixin,generic.DeleteView):
    model=Home
    template_name='home/post_delete.html'
    success_url=reverse_lazy('list')
    
    
#--------------API---------------
class Api_List_View(generics.ListAPIView):
    queryset=Home.objects.all()
    serializer_class=HomeSeriailzer


