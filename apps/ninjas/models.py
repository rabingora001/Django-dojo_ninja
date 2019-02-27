from __future__ import unicode_literals
from django.db import models

# Create your models here.

class dojo(models.Model):
    name=models.CharField(max_length =255)
    city =models.CharField(max_length=250)
    state= models.CharField(max_length =2)
    desc =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now =True)

    def __unicode__(self):
        return "id : " + str(self.id) + ", name : " + self.name + ", city : " + self.city + ", state : " + self.state


class ninja(models.Model):
    first_name=models.CharField(max_length =255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(dojo, related_name="ninjas")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "id : " + str(self.id) + ", first_name : " + self.first_name + ", last_name : " + self.last_name + ", dojo : " + str(self.dojo.name)
