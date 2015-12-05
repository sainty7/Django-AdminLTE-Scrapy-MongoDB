from django.db import models

# Create your models here.

class Person(models.Model):
        name = models.CharField(max_length=100)
        email = models.CharField(max_length=100)
        passwd = models.CharField(max_length=100)
	photo_url = models.CharField(max_length=100)
#	photo = models.FileField(upload_to='/user')
        def __unicode__(self):
                return self.name

class File(models.Model):
	name = models.CharField(max_length=100)
	person = models.ForeignKey(Person)
#	files = models.FileField(upload_to='/home/mtbf3/')
#        content = models.CharField(max_length=1000)
        note = models.CharField(max_length=100 )
	def __unicode__(self):
		return self.name


