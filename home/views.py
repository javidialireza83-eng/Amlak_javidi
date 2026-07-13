from urllib import response
from django.shortcuts import render
from .models import Home, HomeImage
from .forms import HomeForms
from .seriailzers import HomeSeriailzer
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
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
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        images = self.request.FILES.getlist('images')
        for image in images:
          HomeImage.objects.create(home=self.object, image=image) 
        return response

class Update_View(LoginRequiredMixin,generic.UpdateView):
    model=Home
    # fields='__all__'
    form_class=HomeForms
    template_name='home/post_update.html'
    success_url=reverse_lazy('list')
    
    def dispatch(self, request, *args, **kwargs):
        obj=self.get_object()
        if obj.owner != request.user:
             return HttpResponseForbidden("شما اجازه ویرایش این آگهی را ندارید.")
        return super().dispatch(request, *args, **kwargs)
    
class Detele_View(LoginRequiredMixin,generic.DeleteView):
    model=Home
    template_name='home/post_delete.html'
    success_url=reverse_lazy('list')
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            return HttpResponseForbidden("شما اجازه حذف این آگهی را ندارید.")
        return super().dispatch(request, *args, **kwargs)

#--------------API---------------
class Api_List_View(generics.ListAPIView):
    queryset=Home.objects.all()
    serializer_class=HomeSeriailzer


