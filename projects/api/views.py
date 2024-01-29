from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import generics, permissions

from api.serializers import GroupSerializer, UserSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
