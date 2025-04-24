from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('parking.urls')),
    path('api/v1/', include('vehicles.urls')),
    #incluindo as urls/rotas das apps à api

    path('admin/', admin.site.urls),
]
