# Generated by Django 2.1.1 on 2019-07-03 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'ordering': ['price'], 'verbose_name': 'Смартфон', 'verbose_name_plural': 'Смартфоны'},
        ),
    ]
