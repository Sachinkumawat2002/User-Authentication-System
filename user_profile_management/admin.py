from typing import Any
from django.contrib import admin
from .models import *
from django.contrib.auth.hashers import make_password
# Register your models here.

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display=["id","username","email","phone_number"]
    search_fields = ["username"]      

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not change and not obj.pk:
            obj.password = make_password(obj.password)
        elif change and obj.password!= obj.__class__.objects.get(pk = obj.pk).password:
            obj.password = make_password(obj.password)
        return super().save_model(request, obj, form, change) 

  

#  user ---  admin
#  pwd ----  admin@12