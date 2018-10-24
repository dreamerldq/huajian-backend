from django.urls import path

from . import views
urlpatterns = [
    path('list_invoice', views.invoice_list),
    path('create_invoice', views.create_invoice),
    path('delete_invoice', views.delete_invoice),
    path('update_state', views.update_state),





    # path('affirm_invoice', views.affirm_invoice),
    # path('affirm_invoice_list', views.getAffirmInvoiceList)
]
