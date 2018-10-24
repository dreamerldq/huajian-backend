from django.shortcuts import render
from django.utils import timezone
from users.models import User
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from utils import *
# Create your views here.


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

    return JsonResponse({
        'status':'success',
        'data': json.loads(resData)
    })
