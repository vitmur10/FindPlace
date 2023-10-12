from django.db import models


# Create your models here.

class Region(models.Model):
    name_region = models.CharField(max_length=100)
    about_region = models.TextField()

    def __str__(self):
        return self.name_region


class Location(models.Model):
    TYPE_CHOICES = (
        ('Активний відпочинок', 'Активний відпочинок'),
        ('Їжа та напої', 'Їжа та напої'),
        ('Природа та ландшафти', 'Природа та ландшафти'),
        ('Панорамні види', 'Панорамні види'),
        ('Площа', 'Площа'),
        ('Готелі та місця для проживання', 'Готелі та місця для проживання'),
        ('Музеї та виставки', 'Музеї та виставки'),
        ('Церкви та місця релігійного значення', 'Церкви та місця релігійного значення'),
        ("Достопримічальності та пам'ятки", "Достопримічальності та пам'ятки"),
        ('Інше', 'Інше'),
        ('Забуті місця', 'Забуті місця'),
    )
    name_location = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    about = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    cost = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='location_photos/', blank=True, null=True)
    address = models.CharField(max_length=200)
    map_link = models.URLField()
    route = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_location
