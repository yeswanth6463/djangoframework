# Generated by Django 5.1.5 on 2025-03-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_id', models.IntegerField()),
                ('train_name', models.CharField(max_length=100)),
                ('starting_from', models.TimeField()),
                ('ending_at', models.TimeField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('toatl_stops', models.IntegerField()),
                ('food_avilaibility', models.BooleanField()),
                ('sleeper_class', models.BooleanField()),
                ('ac_class', models.BooleanField()),
            ],
        ),
    ]
