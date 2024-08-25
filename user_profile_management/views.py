from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status , viewsets
from rest_framework.response import Response
from rest_framework import status
from core.pagination import UserPagination
from core.permissions import *
# Create your views here.


class CreateuserViewSet(viewsets.ModelViewSet):
    serializer_class = User1Serializer
    http_method_names=["post"]
    def get_queryset(self):
        return UserProfile.objects.none()

class UserAuthViewSet(viewsets.ModelViewSet):
    serializer_class = UserPermissionSerializer
    http_method_names=["post"]

    def get_queryset(self):
        return UserProfile.objects.none()
    
    def create(self, request, *args, **kwargs):
        response = tokenControl(request,UserProfile,UserPermissionSerializer)
        token = response.data["token"]
        print(token)
        if token:
            return Response({f"token:{token}"})                    
        else:
            return Response("Invalid Credential")    
        

class AllUserViewSet(viewsets.ModelViewSet):
    serializer_class = AllUsersSerializer
    pagination_class = UserPagination
    permission_classes = [UserPermission]
    http_method_names = ["get"]    

    def get_queryset(self):
        return UserProfile.objects.all()

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = UserPagination
    http_method_names = ["get"] 
    permission_classes = [UserPermission]
   

    def retrieve(self, request, pk=None):
        try:
            user_profile = UserProfile.objects.get(pk=pk)
            serializer = self.get_serializer(user_profile)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)




class UserProfileUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = UserUpdateSerializer
    pagination_class = UserPagination
    http_method_names = ["get","patch","delete"] 
    permission_classes = [UserPermission]

    def list(self, request, *args, **kwargs):
        user = UserProfile.objects.filter(id=request.user["id"]).first()
        # print(user)
        serializer = UserProfileSerializer(user,many=False)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        # instance = request.user
        print(request.user["id"])
        user = UserProfile.objects.filter(id=request.user["id"]).first()
        # if request.data.get('password'):
        # request.data['password'] = make_password(request.data["password"])

        serializer = UserUpdateSerializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        serializer.save()
        return Response(serializer.data)