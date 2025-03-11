from django.db import models
from core.base import BaseModel
# Create your models here.


class Department(BaseModel):
    name = models.CharField(max_length=180)
    
    def __str__(self):
        return self.name
    