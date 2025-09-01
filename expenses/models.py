from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    """Represents a financial expense linked to a category."""

    category = models.ForeignKey(Category, related_name='expenses', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    expense_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category} {self.amount}"