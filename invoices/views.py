from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from utils import *
from .models import Invoice, User
import json
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
# Create your views here.


def index(request):
    try:
        invoices = Invoice.objects.all()
    except 'OperationalError':
        return HttpResponse('没有数据')
    else:
        data_dir = query_set_to_dir(invoices)
        # data = json.loads(serializers.serialize('json', invoices))
        # data_dir = list(map(res_data, data))
        response = {
            'data': data_dir,
            'status': 'success'
        }
        return JsonResponse(response)


def create_user(request):
    user_data = json.loads(request.body)
    print("啊啊啊啊啊", user_data)
    user = User(
        username=user_data['userName'],
        password=user_data['password'],
        phone_number=user_data['phone_number'],
        email=user_data['email']
    )
    user.save()
    response = {
        'status': 'success'
    }
    return JsonResponse(response)


def checked_login(request):
    name = request.POST.get('userName')
    print(request.body)
    post_data = json.loads(request.body)
    print("AAAAAA", post_data)
    user = User.objects.get(username=post_data['userName'])
    print("账号", user)
    if user.password == post_data['password']:
        return JsonResponse({
            'status': 'success'
            })
    else:
        return HttpResponse('请重新确认用户名或密码')

def create(request):
    post_data = json.loads(request.body)
    invoice = Invoice(
        invoice_type=post_data['invoice_type'],
        money=post_data['money'],
        project_principle=post_data['project_principle'],
        project_name=post_data['project_name'],
        company_name=post_data['company_name'],
        taxpayer_id=post_data['taxpayer_id'],
        address=post_data['address'],
        phone_number=post_data['phone_number'],
        bank=post_data['bank'],
        bank_user=post_data['bank_user'],
        remark=post_data['remark']
    )
    user = User.objects.get(username=invoice['project_principle'])
    invoice.user = user
    invoice.save()
    invoices = Invoice.objects.all()
    invoice = query_set_to_dir(invoices)[-1]
    response = {
        'data': invoice,
        'status': 'success'
    }
    return JsonResponse(response)
