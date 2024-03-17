from django.contrib.auth.models import User

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from merchant_auth.models import Merchant
from merchant_auth.serializers import merchant_serializers
from merchant_auth.serializers import user_serializers

from merchant_auth.models import Application
from merchant_auth.serializers import application_serializers

class GetMerchantView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = user_serializers.UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateMerchantView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = merchant_serializers.MerchantCreateSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.queryset.get(username=request.data['username'])

        refresh = RefreshToken.for_user(user)

        data = {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "username": user.username,
            "email": user.email,
            "email_verified": user.merchant.email_verified
        }
        return Response(data, status=status.HTTP_201_CREATED)
    

class UpdateMerchantView(generics.UpdateAPIView):
    serializer_class = merchant_serializers.UpdateMerchantSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Merchant.objects.get(user=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        serializer.save(merchant=instance)


class GetApplicationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        merchant = request.user.merchant
        applications = Application.objects.filter(merchant=merchant)
        serializer = application_serializers.ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateApplicationView(generics.CreateAPIView):
    serializer_class = application_serializers.CreateApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(merchant=self.request.user.merchant)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class UpdateApplicationView(generics.UpdateAPIView):
    pass
#     serializer_class = merchant_serializers.UpdateMerchantSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return Merchant.objects.get(user=self.request.user)

#     def perform_update(self, serializer):
#         instance = self.get_object()
#         serializer.save(merchant=instance)