
from django.urls import include, path

urlpatterns = [
    path('cakes/', include('cakes.urls')),
    path('admins/', include('admins.urls')),
    path('', include('accounts.urls'))
    ]
