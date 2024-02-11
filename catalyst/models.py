from django.db import models

# Create your models here.

class UploadedData(models.Model):
    data_file = models.FileField(upload_to='uploads/')