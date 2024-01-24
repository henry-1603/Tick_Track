from django.db import models
from django.contrib.auth.models import User
# Create your models here.
choice = (
    ("True" , "True"),
    ("False" , "False"),
)

class Task(models.Model):
    # Foreign keys is used for many to one
    user = models.ForeignKey(User , on_delete=models.CASCADE) # cascade is to known to delete
    title = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    complete =  models.BooleanField(default=False)
    created =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["complete"]
