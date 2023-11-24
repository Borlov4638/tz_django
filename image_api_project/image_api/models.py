from django.db import models

class Image(models.Model):
    description = models.TextField()
    base64_data = models.TextField()
