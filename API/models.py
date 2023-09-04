from django.db import models

# Category model to categorize tasks
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    



# Task model to represent individual tasks
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title