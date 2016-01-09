from django.db import models

# Create your models here.

class Container(models.Model):
	_id = models.IntegerField(max_length=100)	
	

class Person(models.Model):
        name = models.CharField(max_length=100)
        email = models.CharField(max_length=100)
        passwd = models.CharField(max_length=100)
	identity = models.IntegerField(max_length=100)
	_id = models.IntegerField(max_length=100)
	container_id = models.ForeignKey(Container)
	sex = models.CharField(max_length=100)

        def __unicode__(self):
                return self.name

class File(models.Model):
	name = models.CharField(max_length=100)
	person = models.ForeignKey(Person)
        note = models.CharField(max_length=100 )
	def __unicode__(self):
		return self.name


