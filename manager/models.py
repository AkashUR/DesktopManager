from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    log_key = models.IntegerField()

    def __str__(self):
        return self.name+' - '+self.ip+' - '+str(self.log_key)

class Log(models.Model):
    log_key = models.IntegerField(default='1')
    action = models.CharField(max_length=20)
    element = models.CharField(max_length=50,default='null')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.action+' - '+self.element+' - '+str(self.date)+' - '+str(self.time)





