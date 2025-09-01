from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from categories.models import Category
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySummarySerializer, TopCategorySerializer

# Create your views here.
class TopThreeCategoriesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        top_three_cat = Category.objects.annotate(total_amount = Sum('expenses__amount')).order_by("-total_amount")[:3]
        serializer = TopCategorySerializer(top_three_cat, many=True)
        return Response({"message":"Top Three Categories","data": serializer.data}, status=status.HTTP_200_OK)


class CategorySummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.annotate(used = Sum('expenses__amount')).values("id", "name", "max_limit", "used")
        summary = []
        for cat in categories:
            used = cat["used"] or 0 
            remaining = cat["max_limit"] - used
            summary.append({
                "id": cat["id"],
                "name": cat["name"],
                "max_limit": cat["max_limit"],
                "used": used,
                "remaining": remaining
            })
        
        serializer = CategorySummarySerializer(summary, many=True)
        return Response({"message":"Categories Summary", "data":serializer.data}, status=status.HTTP_200_OK)