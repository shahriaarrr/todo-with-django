from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignupSerializer

class SignupAPIView(APIView):
    def post(self, request):
        signup_serializer = SignupSerializer(data=request.data)
        if signup_serializer.is_valid():
            signup_serializer.save()
            return Response({'message' : 'User successfully signed up'})

        return Response({'message' : signup_serializer.errors})