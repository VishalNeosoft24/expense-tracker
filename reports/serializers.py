from rest_framework import serializers

class CategoryMonthlyExpenseSerializer(serializers.Serializer):
    name = serializers.CharField()
    spent = serializers.DecimalField(max_digits=10, decimal_places=2)


class MonthlyExpenseSerializer(serializers.Serializer):
    month = serializers.CharField()
    total_expense = serializers.DecimalField(max_digits=10, decimal_places=2)
    categories = CategoryMonthlyExpenseSerializer(many=True)
