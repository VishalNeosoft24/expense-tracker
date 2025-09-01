from django.db import models

# Create your models here.
class Category(models.Model):
    """Represents an expense category that can be assigned to expenses."""
    
    name = models.CharField(max_length=50)
    max_limit = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name