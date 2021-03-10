from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import random
import string
# Create your views here.
from django.views import View
import json
from project1.models import Project
from interfaces.models import Interfaces
from django.db import connection
from django.db.models import Count,Min,Max,Avg
class projectclass(View):
    def get(self,request,pk):
        # pass
        # datas = [
        #     {
        #         "project_name":"前程贷项目1",
        #         "leader":"xiaoming",
        #         "app_name":"p2p"
        #     },
        #     {
        #         "project_name": "前程贷项目12",
        #         "leader": "xiaoming2",
        #         "app_name": "p2p"
        #     },
        #     {
        #         "project_name": "前程贷项目13",
        #         "leader": "xiaoming3",
        #         "app_name": "p2p"
        #     },
        # ]
        # one_project= Project(name='xxx金融项目',leader='xiaoming')
        # one_project.save()
        # one_project=Project.objects.create(name='ob_金额项目',leader='xianggg')
        # Interfaces.objects.create(name="登录接口",tester='hhjh',projects_id=one_project.id)
        # Interfaces.objects.create(name="登录接口", tester='hhjh', projects=one_project)
        # one_project = Project.objects.get(id=5)
        # one_project.name ='修改01'
        # one_project.save()
        # Project.objects.filter(id=5).update(name='xiugai002')
        # one_project =Project.objects.get(id=1)
      #  one_project = Project.objects.filter(id=1)
        #qs = Project.objects.filter(id__gt=4)
        #取出某个项目所属接口名称中包含”登录“的项目i
        #qs =Project.objects.filter(interfaces__name__contains="登录")
        # qs = Interfaces.objects.filter(name__contains="登录")
        # aa=qs[0].name
        #qs = Project.objects.filter(name__contains="项目").filter(name__contains="ob")
       # qs =Project.objects.filter(name__contains="项目",leader__contains="xian")
        #qs = Project.objects.filter(Q(name__contains='金融')|Q(leader__contains="xian"))
        # qs=Project.objects.get(pk=1)
        # qs.delete()
        # qs = Project.objects.filter(name__contains="金融").delete()
        # print(qs)
        # names =['登录接口','注册接口','订单接口','购物车接口']
        # for i in range(20):
        #     random_str =''.join(random.sample(string.ascii_letters+string.digits,8))
        #     interface_name = random.choice(names)+random_str
        #     Interfaces.objects.create(name=interface_name,tester='sssss',projects_id=random.choice([2,3,4,5]))
        #项目下的接口总数--执行聚合运算
        # values和annotate为固定用法
       # qs = Project.objects.values('id').annotate(Count('interfaces'))
        qs = Project.objects.values('id').annotate(interfaces000=Count('interfaces'))
        print(qs)
        return HttpResponse('')
    def post(self,request,pk):
        # json_str = request.body.decode('utf-8')
        # json_dict = json.loads(json_str)
        return HttpResponse(f"jjjjjjj{pk}",content="hello",status=5001)

