from django.db import models


class Field(models.Model):
    sort_number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    width = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CsvPath(models.Model):
    path = models.FilePathField(max_length=200)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.save()

    def __str__(self):
        return self.path
