from rest_framework import serializers
from django.contrib.auth.hashers import make_password 


from .models import *
class User1Serializer(serializers.ModelSerializer):
    def create(self,validate):
            # print(validate["password"])
            password = make_password(validate["password"])
            # print(password)
            del validate["password"]
            return UserProfile.objects.create(password=password,**validate)
    class Meta:
        model = UserProfile
        fields = '__all__'

class AllUsersSerializer(serializers.ModelSerializer):
     class Meta:
          model = UserProfile
          fields = ["id","username","email","phone_number","address","profile_picture"]        

class UserProfileSerializer(serializers.ModelSerializer):
        class Meta:
                model = UserProfile
                fields = ["id","username","email","phone_number","address","profile_picture"]


class UserPermissionSerializer(serializers.ModelSerializer):
       class Meta:
          model = UserProfile
          fields = ["email","password"]  



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'






       
                      