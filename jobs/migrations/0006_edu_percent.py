# Generated by Django 2.0.2 on 2020-08-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_edu'),
    ]

    operations = [
        migrations.AddField(
            model_name='edu',
            name='percent',
            field=models.FloatField(default=2),
        ),
    ]