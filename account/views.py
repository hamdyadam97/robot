from rest_framework.response import Response
from rest_framework import status, generics
from .serializer import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, \
  UserChangePasswordSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


class UserRegistrationView(generics.GenericAPIView):
  serializer_class = UserRegistrationSerializer
  renderer_classes = [UserRenderer]
  def post(self, request):
    user = request.data
    serializer = self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)


class UserLoginView(generics.GenericAPIView):
  serializer_class = UserLoginSerializer
  renderer_classes = [UserRenderer]
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get('username')
    password = serializer.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(generics.GenericAPIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  serializer_class = UserLoginSerializer
  def get(self, request):
    serializer = self.serializer_class(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(generics.GenericAPIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  serializer_class = UserChangePasswordSerializer
  def post(self, request):
    serializer = self.serializer_class(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)


class SendPasswordResetEmailView(generics.GenericAPIView):
  renderer_classes = [UserRenderer]
  serializer_class = SendPasswordResetEmailSerializer
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)


class UserPasswordResetView(generics.GenericAPIView):
  renderer_classes = [UserRenderer]
  serializer_class = UserPasswordResetSerializer

  def post(self, request, uid,token,):
    serializer = self.serializer_class(data=request.data, context={'uid': uid, 'token': token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)



