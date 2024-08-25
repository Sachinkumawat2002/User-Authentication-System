from django.db import models
from core.validators import *
from core.encrypt_data import *
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from cryptography.fernet import Fernet

class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255, validators=[validate_password])
    address = models.CharField(max_length=255)
#   ##address = models.CharField(max_length=255, validators=[validate_address]) 
    phone_number = models.CharField(blank = True, validators=[validate_phone_number_with_country])
    profile_picture = models.ImageField(upload_to='profile_pics/')

    def save(self, *args, **kwargs):
        fernet = settings.ENCRYPTION_KEY
        self.phone_number = Fernet(fernet).encrypt(self.phone_number.encode()).decode()
        self.address = Fernet(fernet).encrypt(self.address.encode()).decode()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.username
