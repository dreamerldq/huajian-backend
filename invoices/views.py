from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from utils import *
from .models import Invoice, User, AccountList
import json
from django.utils import timezone
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


def affirm_invoice(request):
    post_data = json.loads(request.body)
    money_received = post_data['money_received']
    remark = post_data['remark']
    id = post_data['id']
    invoice = Invoice.objects.get(id=id)
    accountList = AccountList.objects.create(
        invoice=invoice,
        money_received = money_received,
        pay_type = '已付',
        remark = remark,
        create_time = timezone.now()
    )
    accountList.save()
    response = {
        'status': 'success'
    }

def create_user(request):
    user_data = json.loads(request.body)
    user = User(
        username=user_data['userName'],
        password=user_data['password'],
        phone_number=user_data['phone_number'],
        email=user_data['email'],
        create_date=timezone.now()
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
    user = User.objects.get(username=post_data['userName'])
    if user.password == post_data['password']:
        JsonResponse.set_cookie(login=True)
        return JsonResponse({
            'status': 'success'
            })
    else:
        return HttpResponse('请重新确认用户名或密码')

def create(request):
    post_data = json.loads(request.body)
    user = User.objects.get(username=post_data['project_principle'])
    invoice = Invoice.objects.create(
        user=user,
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
        remark=post_data['remark'],
        create_time=timezone.now()
    )
    invoice.save()
    response = {
        'status': 'success'
    }
    return JsonResponse(response)

def delete_invoice(request):
    id = json.loads(request.body)['id']
    invoice = Invoice.objects.get(pk=id)
    invoice.delete()
    invoice.save()
    return JsonResponse({
            'status': 'success'
            })

