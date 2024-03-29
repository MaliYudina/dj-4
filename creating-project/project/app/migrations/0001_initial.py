# Generated by Django 2.2 on 2019-07-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=25)),
                ('longitude', models.FloatField(max_length=25)),
                ('name', models.CharField(max_length=50)),
                ('routes', models.ManyToManyField(related_name='stations', to='app.Route')),
            ],
        ),
    ]
