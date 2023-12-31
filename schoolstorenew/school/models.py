import category as category
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    objects = None
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('school:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    objects = None
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('school:prodCatdetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
    def __str__(self):
        return '{}'.format(self.name)


