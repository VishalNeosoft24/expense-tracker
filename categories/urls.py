from django.urls import path
from .views import CategorySummaryView, TopThreeCategoriesView

urlpatterns = [
    path('top-three-cat/', view=TopThreeCategoriesView.as_view(), name='top-three-cat'),
    path('category-summary/', view=CategorySummaryView.as_view(), name='category-summary'),
]
