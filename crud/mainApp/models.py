from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    salary = models.IntegerField()
    dsg = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20,default = 'Ghaziabad',blank = True)
    state = models.CharField(max_length = 20,default = 'Trainer',blank = True)

    def __str__(self):

        return f"{self.id} {self.name} {self.email}"
