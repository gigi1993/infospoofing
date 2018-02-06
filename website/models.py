from django.db import models
from django.utils import timezone
# Create your models here.
class Visit(models.Model):
    number = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    visited = models.CharField(max_length=120, default='')
    ip_address = models.CharField(max_length=120, default='')
    asn = models.CharField(max_length=15, default='')
    country = models.CharField(max_length=5, default='')

    def __str__(self):
        return "%s %s %s" %(self.visited, self.country, self.asn, self.ip_address)
