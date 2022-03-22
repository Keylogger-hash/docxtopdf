from django.db import models
from uuid import uuid4
# Create your models here.
class FileDocxPdf(models.Model):
    file_id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    type = models.CharField(max_length=1024)
    filename = models.CharField(max_length=1024)
    filepath = models.FilePathField(max_length=1024)
    filepathpdf = models.FilePathField(default='')
    def save(self, *args,**kwargs):
        super().save(*args, **kwargs)