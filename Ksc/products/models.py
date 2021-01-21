from django.db import models
from django.urls import reverse
from Ksc.utils import unique_slug_generator
from django.db.models.signals import pre_save
# Create your models here.



# Catagory
class Catagory(models.Model):
    image =models.ImageField()
    title  =models.CharField(max_length=100)
    slug  =models.SlugField(max_length=100,blank=True,null=True)

    class Meta:
        verbose_name='catagory'
        verbose_name_plural='catagories'

    def get_absoulte_url(self):
        return reverse('post:list_of_catagory',args=[self.slug])

    def __str__(self):
        return str(self.title)

def catagorysignal(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(catagorysignal,sender=Catagory)


#products
class Prod(models.Model):
    image       =models.ImageField()
    title        =models.CharField(max_length=100)
    price       =models.IntegerField()
    catagory    =models.ForeignKey(Catagory,on_delete=models.CASCADE)
    description =models.TextField(max_length=12000)
    status      =models.CharField(max_length=12000,default='publish')
    slug        =models.SlugField(max_length=100,blank=True,null=True)
    def __str__(self):
        return str(self.title)

def prodsignal(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(prodsignal,sender=Prod)

# contactus.
class Contactus(models.Model):
    Name     =models.CharField(max_length=120)
    Email    =models.CharField(max_length=120)
    Phone    =models.IntegerField()
    Message  =models.TextField(max_length=1200)

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name='contactform'
        verbose_name_plural='contact'
