from django.db import models

# Create your models here.

class Todo(models.Model):
    # we don't need to create an id since django does this automatically
    title = models.CharField(max_length=350)
    complete = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    
    