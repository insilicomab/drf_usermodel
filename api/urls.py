from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import CreateUserView, MyProfileView

router = routers.DefaultRouter()

urlpatterns = [
    path('myprofile/', MyProfileView.as_view(), name='myprofile'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('', include(router.urls)),
]
