from rest_framework.serializers import ModelSerializer
from .models import User, Address, History


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ('address', 'latitude', 'longitude')


class HistorySerializer(ModelSerializer):
    class Meta:
        model = History
        fields = ('description', 'updated')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'type', 'phone', 'image_url')


class UserDetailSerializer(ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    histories = HistorySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'type', 'phone', 'email', 'name', 'surname', 'description', 'image_url', 'addresses',
                  'connectedTo', 'histories')


