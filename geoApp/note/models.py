from django.db import models


class Note(models.Model):
    note_heading = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.note_heading
