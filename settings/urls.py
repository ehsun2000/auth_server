from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from user_auth_api.views import UserLoginView

# 設定 API 文檔的基本資訊
schema_view = get_schema_view(
    openapi.Info(
        title="用戶身份驗證和授權API",
        default_version='v1',
        description="用戶身份驗證和授權API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="zhengehsun@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger JSON 或 YAML 文件，可以直接訪問這些文件
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # Swagger UI 路徑，提供可視化界面
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # ReDoc UI 路徑，另一種風格的 API 文檔可視化界面
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # 登入 API 路徑
    path('api/auth/login/', UserLoginView.as_view(), name='user_login'),
]
