from django.shortcuts import render
from django.utils import timezone
import json
from .models import User
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from utils import *
# Create your views here.

def checked_login(request):
    name = request.POST.get('userName')
    print(request.body)
    post_data = json.loads(request.body)
    user = User.objects.get(username=post_data['userName'])
    if user.password == post_data['password']:
        JsonResponse.set_cookie(login=True)
        return JsonResponse({
            'status': 'success'
            })
    else:
        return HttpResponse('请重新确认用户名或密码')

def create_user(request):
    user_data = json.loads(request.body)
    user = User(
        username=user_data['user_name'],
        password=user_data['password'],
        phone_number=user_data['phone_number'],
        email=user_data['email'],
        create_time=timezone.now()
    )
    user.save()
    response = {
        'status': 'success'
    }
    return JsonResponse(response)


def edit_user(request):
    user_data = json.loads(request.body)
    id = user_data['id']
    user = User.objects.get(pk=id)
    user.username = user_data['username']
    user.password = user_data['password']
    user.email = user_data['email']
    user.phone_number = user_data['phone_number']
    user.save()
    response = {
        'status': 'success'
    }
    return JsonResponse(response)




def get_user(request):
    user_data = json.loads(request.body)
    id = user_data['id']
    user = User.objects.filter(id=id)

    user_obj = query_set_to_dir(user)
    response = {
        'data': user_obj,
        'status': 'success'
    }
    return JsonResponse(response)


def delete_user(request):
    user_data = json.loads(request.body)
    id = user_data['id']
    user = User.objects.filter(id=id)
    user.delete()
    response = {
        'status': 'success'
    }
    return JsonResponse(response)
