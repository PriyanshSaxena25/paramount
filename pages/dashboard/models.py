from django.db import models

class ETLJob(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    application = models.CharField(max_length=50)
    source_system = models.CharField(max_length=50)
    downstream_system = models.CharField(max_length=50)