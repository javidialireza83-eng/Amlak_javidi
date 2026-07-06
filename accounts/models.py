from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

#--------------------------------------

def validate_image_size(image):
    max_image=5*1024*1024
    
    if image.size > max_image :
        raise  ValidationError("Each image must be less than 5MB.")

class User (AbstractUser):
    user_family=models.CharField(max_length=100,verbose_name='نام خانوادگی*')
    number_phone=models.CharField(max_length=11,verbose_name='شماره موبایل*')
    national_card=models.CharField(max_length=10,verbose_name='شماره ملی*')
    email=models.EmailField(null=True,blank=True,verbose_name='ایمیل')
    image=models.ImageField(upload_to='image_account',null=True,blank=True,validators=[validate_image_size],verbose_name='پروفایل')
   