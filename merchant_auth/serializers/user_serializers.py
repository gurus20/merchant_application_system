from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from merchant_auth.models import Merchant


class LoginResponseSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        response = {
            'access_token': data.get("access"),
            'refresh_token': data.get("refresh"),
            'username': self.user.username,
            'email': self.user.email,
            'email_verified': self.user.merchant.email_verified
        }
        return response


class MerchantSerializer(serializers.ModelSerializer):
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
            'phone_verified',
            'support_email',
            'email_verified',
            'merchant_id',
            'merchant_name'
        ]


class UserSerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'merchant'
        )
