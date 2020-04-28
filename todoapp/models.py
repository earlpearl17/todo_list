from django.db import models

class TodoListItem(models.Model):
    content = models.TextField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.content
