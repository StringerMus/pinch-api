from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from decimal import Decimal


#Email
class EmailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()
    to_email = serializers.EmailField()
    listing_id = serializers.IntegerField()
    owner = serializers.CharField(max_length=255)
    item_name = serializers.CharField(max_length=255)
    price = MoneyField(
        max_digits=14,
        decimal_places=2,
    )