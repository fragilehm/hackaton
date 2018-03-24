from rest_framework.serializers import ModelSerializer
from .models import Category, Marker


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'image_url')


class MarkerSerializer(ModelSerializer):

    class Meta:
        model = Marker
        fields = ('id', 'description', 'user_image')


class CategoryAttributesSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class DetailedMarkerSerializer(ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Marker
        fields = ('id', 'categories', 'description', 'address', 'latitude', 'longitude', 'isNeed',
                  'user_id', 'user_phone', 'user_email', 'user_name', 'user_surname', 'user_description',
                  'user_image', 'user_connectedTo')
