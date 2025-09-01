from django.urls import path
from .views import MonthlyExpenseReportAPIView

urlpatterns = [
    path("monthly-expenses/", MonthlyExpenseReportAPIView.as_view(), name="monthly-expenses-report"),
]
