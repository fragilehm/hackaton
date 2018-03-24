from rest_framework.serializers import ModelSerializer
from .models import Category, Marker


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'image_url')


class CategoryAttributesSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class MarkerSerializer(ModelSerializer):
    categories = CategoryAttributesSerializer(many=True, read_only=True)

    class Meta:
        model = Marker
        fields = ('id', 'categories', 'description', 'user_image_url', 'status')


class DetailedMarkerSerializer(ModelSerializer):
    categories = CategoryAttributesSerializer(many=True, read_only=True)

    class Meta:
        model = Marker
        fields = ('id', 'categories', 'description', 'address', 'latitude', 'longitude', 'isNeed', 'status',
                  'user_id', 'user_phone', 'user_email', 'user_name', 'user_surname', 'user_description',
                  'user_image_url', 'user_connectedTo')
