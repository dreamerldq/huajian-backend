from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from utils import *
from .models import Invoice
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
        data = json.loads(serializers.serialize('json', invoices))
        data_dir = list(map(res_data, data))
        response = {
            'data': data_dir
        }
        return JsonResponse(response)


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
    invoice.save()
    invoices = Invoice.objects.all()
    invoice = query_set_to_dir(invoices)[-1]
    response = {
        'data': invoice,
        'status': 'success'
    }
    return JsonResponse(response)

