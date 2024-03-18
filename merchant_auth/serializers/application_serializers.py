import secrets
from rest_framework import serializers
from merchant_auth.models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            'application_id',
            'application_name',
            'website_url',
            'is_active',
        )


class CreateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            'application_id',
            'application_name',
            'website_url',
            'is_active'
        )
        read_only_fields = ['is_active']

    def create(self, validated_data):
        validated_data['is_active'] = True 
        return super().create(validated_data)
    

class UpdateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'application_name',
            'website_url',
            'is_active'
        ]

        extra_kwargs = {
            'application_name': {'required': False},
            'website_url': {'required': False},
            'is_active': {'required': False}
        }
    
class ApplicationSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        read_only_fields = ['secret']


    def update(self, instance, validated_data):
        # Generate a new secret
        validated_data['secret'] = secrets.token_hex(32)
        # Perform the update
        return super().update(instance, validated_data)