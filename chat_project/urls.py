# chat_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from chat_project.views import AboutView

schema_view = get_schema_view(
    openapi.Info(
        title="Chat API",
        default_version='v1',
        description="API documentation for the Simple Chat Application",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # User-related endpoints: registration and profile.
    path('api/users/', include('users.urls')),
    # Chat-related endpoints.
    path('api/chat/', include('chat.urls')),
    # About endpoint.
    path('api/about/', AboutView.as_view(), name='about'),
    # JWT Authentication endpoints.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # API documentation endpoints.
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
