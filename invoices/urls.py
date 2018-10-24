from django.urls import path

from . import views
urlpatterns = [
    path('', views.invoice_list),
    path('create', views.create_invoice),
    path('create_expend', views.create_expend),
    path('delete_expend', views.delete_expend),
    path('update_expend_state', views.update_expend_state),
    path('expend_list', views.expend_list),
    path('delete_invoice', views.delete_invoice),
    path('update_state', views.update_state),


    path('create_user', views.create_user),
    path('delete_user', views.delete_user),
    path('edit_user', views.edit_user),
    path('get_user', views.get_user),


    path('checked_user', views.checked_login),
    path('affirm_invoice', views.affirm_invoice),
    path('affirm_invoice_list', views.getAffirmInvoiceList)
]
