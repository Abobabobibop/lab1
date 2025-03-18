from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Configure API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Chat API",
        default_version='v1',
        description="API documentation for the Simple Chat Application",
        contact=openapi.Contact(email="your_email@example.com"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include app-specific routes
    path('api/users/', include('users.urls')),
    path('api/chat/', include('chat.urls')),

    # JWT Authentication endpoints
    path('api/token/', include('rest_framework_simplejwt.urls')),

    # API documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
