from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Category, Marker
from .serializers import CategorySerializer, MarkerSerializer, DetailedMarkerSerializer, MarkerWithoutImageSerializer


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
        markers1 = Marker.objects.filter(categories=pk, user_image_url__isnull=False)
        markers_serializer1 = MarkerSerializer(markers1, many=True)

        markers2 = Marker.objects.filter(categories=pk, user_image_url__isnull=True)
        markers_serializer2 = MarkerWithoutImageSerializer(markers2, many=True)

        result = markers_serializer1.data + markers_serializer2.data
        return Response(result, status=status.HTTP_200_OK)


class NeedMarkerListByCategoryID(APIView):
    """View to list of actions by category id"""
    def get(self, request, pk, format=None):
        """Check if category exists"""
        try:
            Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        """If exists then return list of markers by category id"""
        markers1 = Marker.objects.filter(categories=pk, user_image_url__isnull=False, isNeed=True)
        markers_serializer1 = MarkerSerializer(markers1, many=True)

        markers2 = Marker.objects.filter(categories=pk, user_image_url__isnull=True, isNeed=True)
        markers_serializer2 = MarkerWithoutImageSerializer(markers2, many=True)

        result = markers_serializer1.data + markers_serializer2.data
        return Response(result, status=status.HTTP_200_OK)


class WantMarkerListByCategoryID(APIView):
    """View to list of actions by category id"""
    def get(self, request, pk, format=None):
        """Check if category exists"""
        try:
            Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        """If exists then return list of markers by category id"""
        markers1 = Marker.objects.filter(categories=pk, user_image_url__isnull=False, isNeed=False)
        markers_serializer1 = MarkerSerializer(markers1, many=True)

        markers2 = Marker.objects.filter(categories=pk, user_image_url__isnull=True, isNeed=False)
        markers_serializer2 = MarkerWithoutImageSerializer(markers2, many=True)

        result = markers_serializer1.data + markers_serializer2.data
        return Response(result, status=status.HTTP_200_OK)


class MarkerDetail(generics.RetrieveAPIView):
    """View to detailed marker information"""
    serializer_class = DetailedMarkerSerializer

    def get_object(self):
        ob = get_object_or_404(Marker, id = self.kwargs['pk'])
        return ob
