from django.db import models

# Create your models here.

class TrainDetails(models.Model):
    train_id = models.IntegerField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    starting_from = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    start_time = models.TimeField()
    reach_time = models.TimeField()
    total_stops = models.IntegerField()
    food_availability = models.BooleanField(default=False)
    general_price = models.DecimalField(max_digits=10, decimal_places=2)
    sleeper_price = models.DecimalField(max_digits=10, decimal_places=2)
    ac_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.train_id} - {self.name}"
