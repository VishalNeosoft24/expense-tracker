from rest_framework import serializers
from categories.models import Category

class TopCategorySerializer(serializers.ModelSerializer):
    # total_amount comes from annotation in queryset
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Category
        fields = ['id', 'name', 'total_amount']


class CategorySummarySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    max_limit = serializers.IntegerField()
    used = serializers.IntegerField()
    remaining = serializers.IntegerField()
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
