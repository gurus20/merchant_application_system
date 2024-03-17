from django.contrib.auth.models import User
from rest_framework import serializers
from merchant_auth.models import Merchant

class MerchantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        return user
    

class UpdateMerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = [
            'company_name',
            'industry',
            'address',
            'pincode',
            'state',
            'country',
            'phone',
            'phone_country_code',
            'support_email',
            'merchant_name'
        ]