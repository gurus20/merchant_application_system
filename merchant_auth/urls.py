from django.urls import path
from merchant_auth import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView
from merchant_auth.serializers import merchant_serializers
from merchant_auth.serializers import user_serializers


urlpatterns = [
    # path("/admin", views, name="superuser"),
    path('auth/login', TokenObtainPairView.as_view(
            serializer_class=user_serializers.LoginResponseSerializer), name='token_obtain_pair'),
    path('auth/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path("merchant/get", views.GetMerchantView.as_view(), name="get_merchant"),
    path("merchant/create", views.CreateMerchantView.as_view(), name="create_merchant"),
    path("merchant/update", views.UpdateMerchantView.as_view(), name="update_merchant"),
]
