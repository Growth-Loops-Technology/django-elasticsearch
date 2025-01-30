from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'categories'
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'subcategories'
    def __str__(self):
        return self.name   
    
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    class Meta:
        db_table = 'product'
    def __str__(self):
        return self.name
        