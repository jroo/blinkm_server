from django.db import models

class CurrentScript(models.Model):
    script = models.IntegerField(null=True)
    