# Create your models here.
from email.policy import default
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
#Create your models here.
PROFESSION_CHOICES =[
    ("Employee","Employee"),
    ("Business","Business"),
    ("Student","Student"),
    ("Other","Other")
]

class moneyType(models.Model):
    name = models.CharField(max_length=50)
    remaks = models.CharField(max_length=50)
    created = models.DateTimeField()
    

    def __str__(self):
        return self.name

class expType(models.Model):
    name = models.CharField(max_length=50)
    c_Type = models.ForeignKey(moneyType, on_delete=models.CASCADE)
    remark = models.CharField(max_length=200)    
    
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("expType_detail", kwargs={"pk": self.pk})

class money(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money_type = models.ForeignKey(moneyType,on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    Date = models.DateField(default = now)
    Category = models.ForeignKey(expType, on_delete=models.CASCADE)

    def __str__(self):
        return self.Category.name
    
        

    
        
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profession = models.CharField(max_length = 10, choices=PROFESSION_CHOICES)
    Savings = models.IntegerField( null=True, blank=True)
    income = models.BigIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image',blank=True,default='profile_image/Trackexpence.png')
    def __str__(self):
        return f"Profile of {self.user.username}"
   

