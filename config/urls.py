from django.contrib import admin
from django.urls import path, include

from network.views import MyTokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("network/", include(('network.urls', 'network'))),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
