from django.contrib import admin

from .models import moneyType, expType,money,UserProfile
# Register your models here.

admin.site.register(expType)
admin.site.register(money)
admin.site.register(UserProfile)
admin.site.register(moneyType)