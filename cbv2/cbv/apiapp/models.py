from django.db import models

# Create your models here.
class TrainDetails(models.Model):
    train_id=models.IntegerField()
    train_name=models.CharField(max_length=100)
    starting_from=models.CharField(max_length=100)
    ending_at=models.CharField(max_length=100)
    start_time=models.TimeField()
    end_time=models.TimeField()
    total_stops=models.IntegerField()
    food_avilaibility=models.BooleanField()
    sleeper_class=models.BooleanField()
    ac_class=models.BooleanField()

    def __str__(self):
        return self.train_name

