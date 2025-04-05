from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from ..serializers import ProfileSerializer, UserSerializer
from ..models import User
from permissions import IsSuperUser
from rest_framework.response import Response
from rest_framework import status


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsSuperUser]
    queryset = User.objects.all()

    
    
    