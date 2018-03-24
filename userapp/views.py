from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserDetailSerializer, UserSerializer


class UserList(APIView):
    """View to list users"""

    def get(self, request, format=None):
        """View to list of users"""
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)


class UserDetail(generics.RetrieveAPIView):
    """View to detailed user information"""
    serializer_class = UserDetailSerializer

    def get_object(self):
        ob = get_object_or_404(User, id=self.kwargs['pk'])
        return ob
