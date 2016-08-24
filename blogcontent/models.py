from __future__ import unicode_literals
from django.db import models

class blog_content(models.Model):
	blog_text=models.TextField()
	blog_head=models.CharField(max_length=100)
#todo any kind of the field adn custom field.
# Create your models here.
