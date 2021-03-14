import json

from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
import random
import string
# Create your views here.
from django.views import View
from project1.models import Project
#创建5个接口

class ProjectViews(View):
    def get(self,request):
        # 1 需要能获取到项目的列数数据（获取所有数据）GET /project1/
        # 2 从数据库中获取到所有项目数据（查询集对象）
        qs = Project.objects.all()
        # 3 查询集转化为json数据
        projects_dict=[ ]
        for obj in qs:
            project_dict={
                'id':obj.id,
                'name':obj.name,
                'leader':obj.leader
            }
            projects_dict.append(project_dict)
        # projects_json=json.dumps(projects_dict,ensure_ascii=False)

        # 将数据进行返回
        return JsonResponse(projects_dict,safe=False,json_dumps_params={"ensure_ascii":False})
    def post(self, request: HttpRequest):
        # 能够创建项目（创建一个项目）
        # url: /projects/
        # method：POST
        # request data: json
        # response data: json
        err_msg = {
            "status": False,
            "msg": "参数错误",
            "num": 0
        }
        #1 获取json参数并转化为python中的数据类型（字典或者或者嵌套字典的列表）
        try:
            json_str = request.body.decode('utf-8')
            python_data=json.loads(json_str)

        except Exception:
            return JsonResponse(err_msg,json_dumps_params={"ensure_ascii":False},status=400)
        #2 需要进行大量的数据校验
        if 'name' not in python_data or len(python_data.get('name'))>20:
            #项目名称的判断
            return JsonResponse(err_msg,json_dumps_params={"ensure_ascii":False},status=400)
        #3 创建项目的数据
        # Project.objects.create(name=python_data.get('name'),leader=python_data.get('leader'))
        #方法二
        obj = Project(**python_data)
        obj.save()
        #4 将创建成功的项目模型对象转化为json数据（对象）
        project_dict={
            'id': obj.id,
            'name': obj.name,
            'leader': obj.leader
        }
        #5 json数据返回前端
        return JsonResponse(project_dict,json_dumps_params={"ensure_ascii": False})
class ProjectDetailView(View):
    # 需要能获取到项目的详情数据（获取前端指定某一条数据）
    # url: /projects/<int:pk>/
    # method：GET
    # response data: json
    def get(self,request,pk):
        # 1 从数据库中获取一条项目数据
        # 2 数据校验
        err_msg = {
            "status": False,
            "msg": "参数错误",
            "num": 0
        }
        try:
            obj = Project.objects.get(id=pk)
        except Exception:
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)
        # 3 将获取的模型类对象转化为json数据
        project_dict = {
            'id': obj.id,
            'name': obj.name,
            'leader': obj.leader
        }
        # 4 将json数据返回前端
        return JsonResponse(project_dict, json_dumps_params={"ensure_ascii": False})

    # 能够更新项目（只更新某一个项目）
    # url: / projects / < int: pk > /
    # method：PUT
    # request
    # data: json
    # response
    # data: json
    def put(self,request,pk):
        err_msg = {
            "status": False,
            "msg": "参数错误",
            "num": 0
        }
        # 1、将获取的模型类对象转化为json数据
        try:
            json_str = request.body.decode('utf-8')
            python_data=json.loads(json_str)

        except Exception:
            return JsonResponse(err_msg,json_dumps_params={"ensure_ascii":False},status=400)
        # 2、需要数据校验
        if 'name' not in python_data or len(python_data.get('name')) > 20:
            # 项目名称的判断
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)
        # 3、获取待更新的模型类对象
        # 4、需要校验pk是否存在
        try:
            obj = Project.objects.get(id=pk)
        except Exception:
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)

        # 5 、数据更新
        obj.name = python_data.get('name') or obj.name  #or obj.name 表示不更新项目名称
        obj.leader = python_data.get('leader') or obj.leader
        obj.save()
        # 6、将更新后的模型类对象转化为json数据
        project_dict = {
            'id': obj.id,
            'name': obj.name,
            'leader': obj.leader
        }
        return JsonResponse(project_dict, json_dumps_params={"ensure_ascii": False},status=201)

    # 能够删除项目（只删除某一个项目）
    # url: / projects / < int: pk > /
    # method：DELETE
    def delete(self,request,pk):
        err_msg = {
            "status": False,
            "msg": "参数错误",
            "num": 0
        }
        # 获取待删除的模型类对象
        # 校验数据
        try:
            obj = Project.objects.get(id=pk)
        except Exception:
            return JsonResponse(err_msg, json_dumps_params={"ensure_ascii": False}, status=400)
        # 删除数据
        obj.delete()
        #将删除成功的信息返回
        sucess_msg ={
            "status":True,
            "msg":"删除成功",
            "num":1
        }
        return JsonResponse(sucess_msg, json_dumps_params={"ensure_ascii": False}, status=204)


