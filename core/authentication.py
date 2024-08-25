from django.contrib.auth.hashers import make_password ,check_password
import jwt 
import uuid
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotAuthenticated,APIException
from user_profile_management.models import *
from django.conf import settings


def generateToken(request,model,serializer):
    if "Authorization" not in request.headers:
            # print("Authorization")
            raise NotAuthenticated
    
    else:    
        token = request.headers["Authorization"]
        # print("Token",token)
        try:
            decode_token = jwt.decode(jwt = token , key = settings.SECRET_KEY, algorithms=["HS256"])
            print(settings.SECRET_KEY)
            user = model.objects.filter(email = decode_token["email"]).first()
            # print(user)
            if user:
                ser = serializer(user,many=False)
                # print(ser)
                # if ser.is_valid():
                return Response(ser.data)
            else:
                # print("False")
                return Response("Invalid Token", status=status.HTTP_400_BAD_REQUEST)
        except:
            # print("except")
            raise NotAuthenticated 

def tokenControl(request,model,serializer):
    if 'email' not in request.data or 'password' not in request.data:
        return Response("Email and password are required", status=status.HTTP_400_BAD_REQUEST)
    user = model.objects.filter(email = request.data["email"]).first()
    if check_password(request.data["password"],user.password):
        token = jwt.encode({"email":user.email,"Sachin":str(uuid.uuid4)},settings.SECRET_KEY,algorithm="HS256")
        # print("Token",token)
        return Response({"token": token}, status=status.HTTP_200_OK)
    else:
        return Response("Invalid Crediationals",status=status.HTTP_400_BAD_REQUEST)
     
     
               
