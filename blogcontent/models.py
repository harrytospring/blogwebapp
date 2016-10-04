from __future__ import unicode_literals
from django.db import models

class timeNode(models.Model):
	typechoice=(
		('year','year'),
		('month','month'),
		('week','week'),
		('day','day'),
		)
	type=models.CharField(max_length=5,choices=typechoice,default="unknownTime")
	time=models.DateField(auto_now=False,auto_now_add=False)
	todoList=models.CharField(max_length=2000)
	doneList=models.CharField(max_length=2000)
#todo any kind of the field adn custom field.
# Create your models here.
