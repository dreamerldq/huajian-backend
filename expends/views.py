from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from utils import *
from users.models import User
from expends.models import Expend
import json
from mysite.utils import createBasicUser
from django.utils import timezone
from django.core.mail import send_mail
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
    print("执行支出查找")
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

