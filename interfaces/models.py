from django.db import models

# Create your models here.
class Interfaces(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="id主键",help_text="id主键")
    name = models.CharField(verbose_name='接口名称',help_text='接口名称',max_length=20)
    tester = models.CharField(verbose_name='测试人员',help_text='测试人员',max_length=10)
    projects = models.ForeignKey('project1.Project',on_delete=models.CASCADE)