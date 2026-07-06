from django.shortcuts import render
from django.views import generic
from .models import User
from .forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView,PasswordResetView,PasswordResetConfirmView

# Create your views here.


#_________Register_______________
class Register_View(generic.CreateView):
    model=User
    form_class=UserForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
    
#_________password_change__________
class Password_change_View(PasswordChangeView):
    model=User
    template_name='registration/passwod_change_form.html'

#__________password_reset____________
class password_reset(PasswordResetView):
    model=User
    template_name='registration/passwod_reset_form.html'

class password_reset_confirm(PasswordResetConfirmView):
    model=User
    template_name='registration/passwod_reset_comfirm.html'
    
#_________profileUser_______________
class profile_user(LoginRequiredMixin,generic.DetailView):
    model=User
    template_name='accounts/profile.html'
    context_object_name='porfile'
       
    def get_object(self):
        return self.request.user