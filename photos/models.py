from unicodedata import category
from django.db import models




# # Create your models here.
# class Category(models.Model): # The Category class inherits from the Model class
#     name = models.CharField(max_length=200, null=False, blank=False)
#     def __str__(self):
#         return self.name
    
#         """
#         The Category class inherits from the Model class
#         """

# class Photo(models.Model): # inherits from the Model class
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
#     image = models.ImageField(null=False, blank=False)
#     description = models.TextField()
#     def __str__(self):
#         return self.description
    
#         """
#         The photo class inherits from the Model class
#         """
        
class Category(models.Model):
    name = models.CharField(max_length=100, null=False,blank=False)
    
    def __str__(self):
        return self.name
 
class Location(models.Model):
    name = models.CharField(max_length=100, null=False,blank=False)
    
    def __str__(self):
        return self.name   

    
class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL, null=True, blank=False)
    image = models.ImageField(null=False,blank=False)
    description = models.TextField()
    
    def __str__(self):
        return self.description
    

