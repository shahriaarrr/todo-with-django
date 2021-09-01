from account.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import SignupSerializer

class SignupAPIView(APIView):
    def post(self, request):
        signup_serializer = SignupSerializer(data=request.data)
        if signup_serializer.is_valid():
            data = signup_serializer.validated_data
            User.objects.create_user(**data)
            return Response({'message' : 'User successfully signed up'})

        return Response({'message' : signup_serializer.errors})

class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data={'message': f"Bye {request.user.username}!"})