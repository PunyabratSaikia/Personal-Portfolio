from django.db import models

class Job(models.Model):
    Role = models.CharField(max_length = 200, default = 'l')
    summary = models.CharField(max_length=200)
    month_s = models.CharField(max_length = 100, default = 'J')
    month_2 = models.CharField(max_length = 100, default = 'D')
    year1 = models.IntegerField(default = 1)
    year2 = models.IntegerField(default = 2)

class Edu(models.Model):
    Degree = models.CharField(max_length = 200, default = 'l')
    summary = models.CharField(max_length=200)
    year1 = models.IntegerField(default = 1)
    year2 = models.IntegerField(default = 2)
    percent = models.FloatField(default = 2)
    college = models.CharField(max_length=200, default = '1')


class Skills(models.Model):
    name = models.CharField(max_length = 200, default = 'l')
    proficient = models.IntegerField(default = 2)

class Projects(models.Model):
    name = models.CharField(max_length = 200, default = 'l')
    summary = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
