# Generated by Django 3.1.7 on 2021-03-07 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project1', '0002_auto_20210307_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('name', models.CharField(help_text='接口名称', max_length=20, verbose_name='接口名称')),
                ('tester', models.CharField(help_text='测试人员', max_length=10, verbose_name='测试人员')),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.project')),
            ],
        ),
    ]
