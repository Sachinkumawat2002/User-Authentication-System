from django.urls import path,include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()

router.register(r"create-user",views.CreateuserViewSet,basename="create-user")
router.register(r"get-all-user",views.AllUserViewSet,basename="get-all-user")


router.register(r"auth",views.UserAuthViewSet,basename="auth")
router.register(r"get-user-by-id",views.UserProfileViewSet,basename="get-user-by-id")
router.register(r"update-user",views.UserProfileUpdateViewSet,basename="update-user")



urlpatterns = router.urls+[


]