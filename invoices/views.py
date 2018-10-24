from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from utils import *
from invoices.models import Invoice
from users.models import User
from mysite.utils import createBasicUser
from expends.models import Expend
import json
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.



def invoice_list(request):
    try:
        invoices = Invoice.objects.all()
    except Exception as e:
        print("捕获的错误",e)
        return HttpResponse('没有数据')
    else:

        data_dir = query_set_to_dir(invoices)
        response = {
            'data': data_dir,
            'status': 'success'
        }
        return JsonResponse(response)

#
# def affirm_invoice(request):
#     post_data = json.loads(request.body)  # json.loads 将request.body的数据转换为Python的字典类型
#     money_received = post_data['money_received']
#     remark = post_data['remark']
#     id = post_data['id']
#     try:
#         invoice = Invoice.objects.get(id=id)
#     except Exception:
#         return HttpResponse('未能找到用户')
#     else:
#          accountList=AccountList.objects.create(
#           invoice=invoice,
#           money_received=money_received,
#           pay_type='已付',
#           remark=remark,
#           create_time=timezone.now()
#          )
#          accountList.save()
#          return JsonResponse({
#             'status': 'success'
#             })


# def getAffirmInvoiceList(request):
#         receivable_account = AccountList.objects.all()
#         data_dir = transfromData(receivable_account)
#         response = {
#             'data': data_dir,
#             'status': 'success'
#         }
#         return JsonResponse(response)






def create_invoice(request):
    post_data = json.loads(request.body)
    try:
        user = User.objects.get(username=post_data['project_principle'])
    except Exception:
        createBasicUser(post_data['project_principle'])
    else:
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
            state=False,
            bank_user=post_data['bank_user'],
            remark=post_data['remark'],
            create_time=timezone.now()
        )
        invoice.save()
        response = {
            'status': 'success'
        }
        return JsonResponse(response)



def update_state(request):
     id = json.loads(request.body)
     invoice = Invoice.objects.get(pk=id)
     invoice.state = True
     invoice.save()
     send_mail(
            '测试邮件',
            '<a href:http://www.baidu.com.>链接</a>',
            '845790692@qq.com', ['17615160540@163.com'],
            html_message='<a href="http://www.baidu.com">链接</a>',
            fail_silently=False
        )
     return JsonResponse({
            'status': 'success'
            })









def delete_invoice(request):
    id = json.loads(request.body)
    try:

        invoice = Invoice.objects.get(pk=id)
    except Exception:
        return HttpResponse('未能找到对应发票')
    else:

        invoice.delete()
        return JsonResponse({
                'status': 'success'
                })

#
# def resData(obj):
#     obj['fields']['id'] = obj['pk']
#     print("AAAAA", obj)
#     invoice = Invoice.objects.get(pk=obj['fields']['invoice'])
#     obj['fields']['money'] = invoice.money
#     obj['fields']['project_principle'] = invoice.project_principle
#     obj['fields']['project_name'] = invoice.project_name
#     obj['fields']['company_name'] = invoice.company_name
#     obj['fields']['invoice_type'] = invoice.invoice_type
#     return obj['fields']
#
#
# def transfromData(query_set):
#     data = json.loads(serializers.serialize('json', query_set))
#     data_dir = list(map(resData, data))
#     return data_dir
