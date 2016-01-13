from django.db import models

# Create your models here.
class Stage(models.Model):
	title = models.CharField(max_length = 200)
	def __str__(self):
	    return self.title

class Report(models.Model):
	title = models.CharField(max_length = 200)
	startDate = models.DateTimeField('date published')
	endDate = models.DateTimeField('date published')
	description = models.TextField(max_length = 5000, null=True, blank=True)
	stage = models.ManyToManyField(Stage)
	def __str__(self):
	    return self.title
	def completed_stages_count(self):
		return 0

class Process(models.Model):
	stage = models.ForeignKey(Stage, on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	isCompleted = models.BooleanField(default = False)
	def __str__(self):
	    return self.title