from django.db import models
class Basemodel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="项目名称")

    class Meta:
        abstract = True