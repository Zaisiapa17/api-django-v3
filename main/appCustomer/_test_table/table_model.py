from django.db import models

# Create your models here.
class Testing(models.Model):
    class Meta:
        db_table = '_testing'
    testing = models.CharField(max_length=100)