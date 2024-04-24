from rest_framework.views import APIView
from rest_framework.response import Response
from .login_service import user_login
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserLoginView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='用戶名'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='密碼')
            }
        ),
        operation_description='登入 API'
    )
    def post(self, request):
        """
        登入 API
        Description:
            提供使用者登入
        Args:
            request: request - Django request 物件

        Returns:
            Response - 回應訊息
        """
        if user_login(request):
            return Response({'message': '登入成功'})
        else:
            return Response({'message': '無效的用戶名或密碼'}, status=400)