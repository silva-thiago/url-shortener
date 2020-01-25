from django.db import models
from django.utils.timezone import now


class Url(models.Model):
    date_create = models.DateTimeField(default=now, editable=False)
    urlInput = models.CharField(max_length=250, null=True, blank=True)
    urlOutput = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.urlInput + ' - ' + self.urlOutput)
