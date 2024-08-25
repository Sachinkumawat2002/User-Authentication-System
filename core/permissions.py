from user_profile_management.models import *
from user_profile_management.serializers import *
from rest_framework.permissions import BasePermission
from rest_framework import status
from .authentication import *

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        user_data = generateToken(request,UserProfile,AllUsersSerializer)
        # print(user_data.data)
        if user_data is not None:
            request.user = user_data.data
            print(">>>>>>>>>>>>>>>>>>>",request.user)
            return True
        else:
            return False
    