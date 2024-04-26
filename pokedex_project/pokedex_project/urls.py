from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from api.controllers import auth_controller,item_controller  # ou un import spécifique

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/connexion', auth_controller.login_user, name='login'),
    path('api/register', auth_controller.register_user, name='register'),
    path('api/items/<int:id>', item_controller.item_detail, name='item_detail'),
    path('api/items/<int:id>/update', item_controller.update_item, name='update_item'),
    path('api/items/<int:id>/delete', item_controller.delete_item, name='delete_item'),
]

# swagger for doc

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Documentation for API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]