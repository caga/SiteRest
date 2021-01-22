from django.db import models

# Create your models here.
class Product(models.Model):
    Kadin='kd'
    Erkek='er'
    Cocuk='cc'
    EvVeYasam='ev'
    SuperMarket='sp'
    Kozmetik='kz'
    AyakkabiCanta='ac'
    SaatAksesuar='sa'
    Elektronik='el'
    Konfeksiyon='kf'

    productCateories=[
            (Kadin,'Kadın'),
            (Erkek,'Erkek'),
            (Cocuk,'Çocuk'),
            (EvVeYasam,'Ev ve Yaşam'),
            (SuperMarket,'Süper Market'),
            (Kozmetik, 'Kozmetik'),
            (AyakkabiCanta, 'Ayakkabı & Çanta'),
            (SaatAksesuar, 'Saat ve Aksesuar'),
            (Elektronik, 'Elektronik'),
            (Konfeksiyon, 'Konfeksiyon'),
            ]
    product_name=models.CharField(max_length=200)
    product_category=models.CharField(max_length=2,choices=productCateories,default=Kadin)
    # product_code=models.IntegerField()
    # seller=models.
