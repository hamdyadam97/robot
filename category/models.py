from django.db import models

# Create your models here.

THE_TYPE = (
    ['type1','type2'],
    ['type2','type2'],
    ['type3','type3'],
    ['type4','type4'],
    ['type5','type5'],
    ['type6','type6'],
    ['type7','type7'],
)

class Category(models.Model):
    name = models.CharField(max_length=20,)
    the_type = models.CharField(max_length=20,choices=THE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return format(self.name)


class Product(models.Model):
    title = models.CharField(max_length=20,)
    description = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    price = models.CharField(max_length=20,null=True)
    count = models.IntegerField(null=True)



    def __str__(self):
        return format(self.title)


class ImageProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    image = models.ImageField(upload_to=product,null=True)

    def __str__(self):
        return format(self.product)