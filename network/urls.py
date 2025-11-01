from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = "network"
urlpatterns = [
    path("network_list/", views.NetworkList.as_view(), name="network_list"),
    path("new_network/", views.NetworkCreate.as_view(), name="network_create"),
    path(
        "<int:pk>/detail_network/", views.NetworkDetail.as_view(), name="network_detail"
    ),
    path(
        "<int:pk>/delete_network/", views.NetworkDelete.as_view(), name="network_delete"
    ),
    path(
        "<int:pk>/update_network/", views.NetworkUpdate.as_view(), name="network_update"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
