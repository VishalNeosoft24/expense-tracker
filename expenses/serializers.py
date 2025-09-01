from rest_framework.serializers import ModelSerializer
from .models import Expense

class AddExpenseSerializer(ModelSerializer):
    class Meta:
        fields = ["category", "amount", "description", "expense_date"]
        model = Expense
