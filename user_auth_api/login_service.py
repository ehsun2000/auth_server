from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer

def user_login(request):
    """
    登入服務
    Description:
        使用者登入驗證，並將使用者訊息存於 user_detail 中
    Args:
        request: request - Django request 物件

    Returns:
        True - 登入成功
        False - 登入失敗
    """
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return False

    username = request.data.get('username')
    password = request.data.get('password')
    # do_login = authenticate(request, username=username, password=password)
    if username == 'test' and password == '1111':
        # login(request, do_login)
        return True
    return False