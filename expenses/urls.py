from django.urls import path
from .views import AddExpenseView

urlpatterns = [
    path('add-expense/', view=AddExpenseView.as_view(), name='add-expense')
]
