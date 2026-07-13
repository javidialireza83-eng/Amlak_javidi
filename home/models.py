from django.db import models
from django.conf import settings
# Create your models here.


class Home(models.Model):

    PROPERTY_TYPE = (
        ("apartment", "آپارتمان"),
        ("villa", "ویلا"),
        ("land", "زمین"),
        ("office", "اداری"),
        ("shop", "مغازه"),
    )

    STATUS = (
        ("فروش", "فروش"),
        ("اجاره", "اجاره"),
        ("پیش فروش", "پیش فروش"),
    )

    title = models.CharField(
        max_length=200,
        verbose_name="عنوان آگهی* "
    )

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE,
        verbose_name="نوع ملک* "
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        verbose_name="وضعیت* "
    )

    price = models.BigIntegerField(
        verbose_name="قیمت* "
    )

    deposit = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name="رهن"
    )

    rent = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name="اجاره"
    )

    area = models.PositiveIntegerField(
        verbose_name="متراژ* "
    )

    rooms = models.PositiveSmallIntegerField(
        verbose_name="تعداد اتاق* "
    )
    
    hammam=models.IntegerField(verbose_name="تعداد حمام",null=True)
    
    floor = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="طبقه"
    )

    # total_floors = models.PositiveSmallIntegerField(
    #     null=True,
    #     blank=True,
    #     verbose_name="تعداد طبقات"
    # )

    year_built = models.PositiveIntegerField(
        verbose_name="سال ساخت* "
    )

    address = models.TextField(
        verbose_name="آدرس* "
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    owner_name = models.CharField(
        max_length=100,
        verbose_name="نام مالک* "
    )

    owner_phone = models.CharField(
        max_length=15,
        verbose_name="شماره مالک* "
    )

    # is_active = models.BooleanField(
    #     default=True,
    #     verbose_name="فعال"
    # )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='homes'
    )

    # image=models.ImageField(upload_to='image_home',null=True,blank=True)
    def __str__(self):
        return self.title
    
class HomeImage(models.Model):
    home=models.ForeignKey(Home,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to='image_home')
    def __str__(self):
        return self.home.title