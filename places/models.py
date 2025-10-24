from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, db_index=True)
    address = models.TextField(blank=True, default="")

    class Meta:
        verbose_name_plural = "Locations"
        ordering = ['name']

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, db_index=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Places"
        ordering = ['name']

    def __str__(self):
        return self.name
