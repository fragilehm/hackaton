from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Category, Marker
from .serializers import CategorySerializer, MarkerSerializer, DetailedMarkerSerializer


class CategoryList(APIView):
    """View to list of categories"""
    def get(self, request, format=None):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        result = category_serializer.data
        return Response(result, status=status.HTTP_200_OK)


class MarkerListByCategoryID(APIView):
    """View to list of actions by category id"""
    def get(self, request, pk, format=None):
        """Check if category exists"""
        try:
            Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        """If exists then return list of markers by category id"""
        markers = Marker.objects.filter(categories=pk)
        markers_serializer = MarkerSerializer(markers, many=True)
        result = markers_serializer.data
        return Response(result, status=status.HTTP_200_OK)


class MarkerDetail(generics.RetrieveAPIView):
    """View to detailed marker information"""
    serializer_class = DetailedMarkerSerializer

    def get_object(self):
        ob = get_object_or_404(Marker, id = self.kwargs['pk'])
        return ob
