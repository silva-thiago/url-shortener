from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    generated_date = models.DateTimeField(default=now, editable=False)
    url_input = models.CharField(max_length=250, null=True, blank=True)
    url_output = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.url_input + ' - ' + self.url_output)
