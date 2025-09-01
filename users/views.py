from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework import status

# Create your views here.
class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Createad"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error":str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)