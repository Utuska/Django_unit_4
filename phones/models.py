from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.FloatField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    lte_exists = models.BooleanField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True, max_length=50)
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'phones'

    def __str__(self):
        return self.name