# Generated by Django 4.0.4 on 2022-11-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
