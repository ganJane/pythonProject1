from django.db import models
from utils.base_model import Basemodel
# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
class Project(Basemodel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,verbose_name="项目名称")
    leader = models.CharField(max_length=20,verbose_name="dddd")
    class Meta:
        db_table = "t1"
    def __str__(self):
        return  self.name