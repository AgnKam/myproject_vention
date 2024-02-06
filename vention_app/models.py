from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True) # An extra

    def clean(self):
        # Custom validation for due_date
        if self.due_date and self.due_date < timezone.now().date():
            raise ValidationError("Due date cannot be in the past.")

    def save(self, *args, **kwargs):
        self.clean()
        super(Task, self).save(*args, **kwargs)

