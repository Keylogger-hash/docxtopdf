from django.db import models
from uuid import uuid4
# Create your models here.
class FileDocxPdf(models.Model):
    file_id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    type = models.CharField(max_length=255)
    filename = models.TextField()
    filepath = models.TextField()
    filepathpdf = models.TextField(default='')
    def save(self, *args,**kwargs):
        super().save(*args, **kwargs)