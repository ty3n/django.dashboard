from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class Upload(models.Model):
    image = models.FileField(upload_to='images')
    def __str__(self):
        return str(self.pk)

class Line(models.Model):
    line_category = models.CharField(max_length=200)
    line_pn = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Line"
    def __str__(self):
        return self.line_category

class Region(models.Model):
    region_category = models.CharField(max_length=200)
    station_ForeignKey = models.ForeignKey(Line, default=1, verbose_name="Line", on_delete=models.SET_DEFAULT)
    class Meta:
        verbose_name_plural = "Region"
    def __str__(self):
        return self.region_category

class Station(models.Model):
    station_category = models.CharField(max_length=200)
    station_script = models.CharField(max_length=200)
    station_User = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)
    station_ForeignKey = models.ForeignKey(Region, default=1, verbose_name="Region", on_delete=models.SET_DEFAULT)
    station_Status = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Station"
    def __str__(self):
        return self.station_category
