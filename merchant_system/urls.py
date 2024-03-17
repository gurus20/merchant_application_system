from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf', include('rest_framework.urls')),
    path('api/v1/', include('merchant_auth.urls'))
]
