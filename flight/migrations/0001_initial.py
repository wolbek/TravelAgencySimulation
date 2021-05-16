# Generated by Django 3.1.7 on 2021-05-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location1', models.CharField(max_length=100)),
                ('location2', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='flight/images/')),
                ('departuredate', models.DateField()),
                ('returndate', models.DateField()),
                ('departuretime', models.TimeField()),
                ('arrivaltime', models.TimeField()),
                ('duration', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]