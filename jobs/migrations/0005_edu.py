# Generated by Django 2.0.2 on 2020-08-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20200828_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Degree', models.CharField(default='l', max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('year1', models.IntegerField(default=1)),
                ('year2', models.IntegerField(default=2)),
            ],
        ),
    ]
