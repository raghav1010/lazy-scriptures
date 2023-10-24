from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Lazy Scriptures API",
        default_version="v1",
        description="API endpoints for Lazy Scriptures API Course",
        contact=openapi.Contact(email="raghav.tech21@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True, permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Lazy Scriptures API Admin"

admin.site.site_title = "Lazy Scriptures API Admin Portal"

admin.site.index_title = "Welcome to Lazy Scriptures API Portal"
