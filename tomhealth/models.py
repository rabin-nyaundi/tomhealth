from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_images/' ,null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url

