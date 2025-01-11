from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


#Email
class EmailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()
    to_email = serializers.EmailField()
    listing_id = serializers.IntegerField()