from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import User, History
from .serializers import UserDetailSerializer, UserSerializer, UserHistorySerializer


class OrganizationList(APIView):
    """View to list organizations"""

    def get(self, request, format=None):
        """View to list of organizations"""
        users = User.objects.all().filter(type="ORGANIZATION")
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)


class UserDetail(generics.RetrieveAPIView):
    """View to detailed user information"""
    serializer_class = UserDetailSerializer

    def get_object(self):
        ob = get_object_or_404(User, id=self.kwargs['pk'])
        return ob


class UserHistoryList(APIView):
    """View to list of histories by user id"""

    def get(self, request, pk, format=None):
        """Check if user exists"""
        try:
            User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        """If exists then return list of histories by user id"""
        histories = History.objects.filter(user=pk)
        histories_serializer = UserHistorySerializer(histories, many=True)
        result = histories_serializer.data
        return Response(result, status=status.HTTP_200_OK)
