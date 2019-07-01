from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Station(models.Model):
    latitude = models.FloatField(max_length=25)
    longitude = models.FloatField(max_length=25)
    name = models.CharField(max_length=50)
    routes = models.ManyToManyField(Route, related_name="stations")

    def __str__(self):
        return self.name
