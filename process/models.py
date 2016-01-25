from django.db import models

# Create your models here.
class Stage(models.Model):
	title = models.CharField(max_length = 200)
	def __str__(self):
	    return self.title
	def all_processes_count(self):
		allProcess = self.process_set.all()
		return allProcess.count()
	def completed_processes_count(self):
		allProcess = self.process_set.all()
		completedCount = 0
		for ps in allProcess:
			if(ps.isCompleted == True):
				completedCount += 1
		return completedCount
	def isStageCompleted(self):
		if(self.all_processes_count() == self.completed_processes_count()):
			return True
		else:
			return False	

class Report(models.Model):
	title = models.CharField(max_length = 200)
	startDate = models.DateTimeField('date published')
	endDate = models.DateTimeField('date published')
	description = models.TextField(max_length = 5000, null=True, blank=True)
	stage = models.ManyToManyField(Stage)
	def __str__(self):
	    return self.title
	def completed_stages_count(self):
		allStage = self.stage.all()
		completedSatgeCount = 0
		for s in allStage:
			if(s.isStageCompleted() == True):
				completedSatgeCount +=1

		return completedSatgeCount

class Process(models.Model):
	stage = models.ForeignKey(Stage, on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	isCompleted = models.BooleanField(default = False)
	def __str__(self):
	    return self.title