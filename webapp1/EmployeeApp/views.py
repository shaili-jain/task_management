from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import User,Task,Assign
from EmployeeApp.serializers import UserSerializer,TaskSerializer,AssignSerializer


# Create your views here.

@csrf_exempt
def userApi(request,id=0):
    if request.method=='GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user=User.objects.get(u_id=user_data['u_id'])
        user_serializer=UserSerializer(user,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        user=User.objects.get(u_id=id)
        user.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def taskApi(request,id=0):
    if request.method=='GET':
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)

    elif request.method=='POST':
        task_data=JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        task_data = JSONParser().parse(request)
        task=Task.objects.get(t_id=task_data['t_id'])
        task_serializer=TaskSerializer(task,data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        task=Task.objects.get(t_id=id)
        task.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def assignApi(request,id=0):
    if request.method=='GET':
        assigns = Assign.objects.all()
        assigns_serializer = AssignSerializer(assigns, many=True)
        return JsonResponse(assigns_serializer.data, safe=False)

    elif request.method=='POST':
        assign_data=JSONParser().parse(request)
        assign_serializer = AssignSerializer(data=assign_data)
        if assign_serializer.is_valid():
            assign_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        assign_data = JSONParser().parse(request)
        assign=Assign.objects.get(id=task_data['id'])
        assign_serializer=AssignSerializer(assign,data=assign_data)
        if assign_serializer.is_valid():
            assign_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        assign=Assign.objects.get(id=id)
        assign.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)