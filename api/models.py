from django.db import models

class Education(models.Model):
	diploma = models.CharField(
		max_length=50
	)
	institution = models.CharField(
		max_length=50
	)
	startYear = models.PositiveSmallIntegerField()
	endYear = models.PositiveSmallIntegerField()

class Employment(models.Model):
	role = models.CharField(
		max_length=50
	)
	workplace = models.CharField(
		max_length=50
	)
	startYear = models.PositiveSmallIntegerField()
	endYear = models.PositiveSmallIntegerField()
	responsibilities = models.TextField()

class Referee(models.Model):
	name = models.CharField(
		max_length=100
	)
	phone = models.CharField(
		max_length=15,
				blank=True
	)
	email = models.EmailField()

class Skills(models.Model):
	name = models.CharField(
		max_length=50,unique=True
	)
	proficiency = models.PositiveSmallIntegerField(
		choices=[
			(1,'Basic'),
			(2,'Regular'),
			(3,'Expert')
		],
		default=2
	)
