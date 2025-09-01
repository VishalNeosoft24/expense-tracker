# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from expenses.models import Expense
from .serializers import MonthlyExpenseSerializer

class MonthlyExpenseReportAPIView(APIView):
    def get(self, request):
        # Aggregate by month & category
        qs = (
            Expense.objects
            .annotate(month=TruncMonth("expense_date"))
            .values("month", "category__name")
            .annotate(total_spent=Sum("amount"))
            .order_by("month")
        )
        # Restructure into {month: {categories, total_expense}}
        report_data = {}    
        for row in qs:
            month_str = row["month"].strftime("%Y-%m")  # e.g. "2025-07"
            if month_str not in report_data:
                report_data[month_str] = {
                    "month": month_str,
                    "total_expense": 0,
                    "categories": []
                }
            report_data[month_str]["categories"].append({
                "name": row["category__name"],
                "spent": row["total_spent"]
            })
            report_data[month_str]["total_expense"] += row["total_spent"]

        # Serialize response
        serializer = MonthlyExpenseSerializer(list(report_data.values()), many=True)
        return Response(serializer.data)
