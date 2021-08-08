from django.db import models
from django.utils import timezone
# Create your models here.

class counter(models.Model):
    esp_result = models.FloatField(default=0)
    date_created = models.DateField(default=timezone.now)

    def publish(self):
        self.esp_result = timezone.now()
        self.save()

    def __str__(self):
        return'Counter : %f' % self.esp_result