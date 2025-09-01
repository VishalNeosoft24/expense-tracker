from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddExpenseSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AddExpenseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({"message": "Expense Added Successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error":str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)