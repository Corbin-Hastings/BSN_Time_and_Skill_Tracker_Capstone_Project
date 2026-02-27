from django.db import models

from django.conf import settings


class hoursLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='time_entries')
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=300)
    instructor = models.CharField(max_length=50)
    #
    def save(self, *args, **kwargs):

        if self.start_time and self.end_time:
            time_difference = self.end_time - self.start_time
            total_seconds = time_difference.total_seconds()
            calculated_hours = total_seconds / 3600
            self.hours = round(calculated_hours, 2)

        super().save(*args, **kwargs)

