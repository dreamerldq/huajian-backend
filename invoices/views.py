from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from utils import *
from .models import Invoice, User, AccountList, Expend
import json
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.

def createBasicUser(username):
    user = User.objects.create(
            username=username,
            create_time=timezone.now()
        )
    user.save()

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


def affirm_invoice(request):
    post_data = json.loads(request.body)  # json.loads 将request.body的数据转换为Python的字典类型
    money_received = post_data['money_received']
    remark = post_data['remark']
    id = post_data['id']
    try:
        invoice = Invoice.objects.get(id=id)
    except Exception:
        return HttpResponse('未能找到用户')
    else:
         accountList=AccountList.objects.create(
          invoice=invoice,
          money_received=money_received,
          pay_type='已付',
          remark=remark,
          create_time=timezone.now()
         )
         accountList.save()
         return JsonResponse({
            'status': 'success'
            })


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


def create_expend(request):
    post_data = json.loads(request.body)
    try:

        user = User.objects.get(username=post_data['project_principle'])

    except Exception:
        createBasicUser(post_data['project_principle'])
    else:

        expend = Expend.objects.create(
            user=user,
            expend_content=post_data['expend_content'],
            project_principle=post_data['project_principle'],
            project_name=post_data['project_name'],
            expend_money=post_data['expend_money'],
            remark=post_data['remark'],
            create_time=timezone.now()
        )
        expend.save()
        response = {
            'status': 'success'
        }
        return JsonResponse(response)

def update_expend_state(request):
     id = json.loads(request.body)
     try:

        expend = Expend.objects.get(pk=id)
     except Exception:
         return HttpResponse('未能找到对应支出账单')
     else:
         expend.state = True
         expend.save()
         return JsonResponse({
                'status': 'success'
                })

def delete_expend(request):
    id = json.loads(request.body)
    try:

        expend  = Expend.objects.get(pk=id)
    except Exception:
         return HttpResponse('未能找到对应支出账单')
    else:
        expend.delete()
        return JsonResponse({
                'status': 'success'
                })

def expend_list(request):
    try:
        expends = Expend.objects.all()
    except Exception:
        return HttpResponse('没有数据')
    else:
        data_dir = query_set_to_dir(expends)
        # data = json.loads(serializers.serialize('json', invoices))
        # data_dir = list(map(res_data, data))
        response = {
            'data': data_dir,
            'status': 'success'
        }
        return JsonResponse(response)

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


def getAffirmInvoiceList(request):
        receivable_account = AccountList.objects.all()
        data_dir = transfromData(receivable_account)
        response = {
            'data': data_dir,
            'status': 'success'
        }
        return JsonResponse(response)



def getStatisticsList():
     users = User.objects.all

     resData = []
     for user in users:
         invoices_dir = query_set_to_dir(user.invoices_set.all())
         expends_dir = query_set_to_dir(user.expends_set.all())
         invoices_money = 0
         expends_money = 0
         for invoice in invoices_dir:
             invoices_money += invoice.money

         for expend in expends_dir:
             expends_money += expend.expend_money

         user_statics = {
            "income": invoices_money,
            "expend": expends_money,
            "balance": invoices_money - expends_money,
            "project_principle": user.username
         }

        resData.psuh(user_statics)





def resData(obj):
    obj['fields']['id'] = obj['pk']
    print("AAAAA", obj)
    invoice = Invoice.objects.get(pk=obj['fields']['invoice'])
    obj['fields']['money'] = invoice.money
    obj['fields']['project_principle'] = invoice.project_principle
    obj['fields']['project_name'] = invoice.project_name
    obj['fields']['company_name'] = invoice.company_name
    obj['fields']['invoice_type'] = invoice.invoice_type
    return obj['fields']


def transfromData(query_set):
    data = json.loads(serializers.serialize('json', query_set))
    data_dir = list(map(resData, data))
    return data_dir
