from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=30, blank=False)
    Email = models.EmailField(blank=False)
    mobile_no = models.BigIntegerField(blank=False)
    username = models.CharField(max_length=40, blank=False, unique=True)
    password = models.CharField(max_length=30, blank=False)
    otp = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.Name
    
    
 
