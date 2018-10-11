from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('delete_invoice', views.delete_invoice),
    path('create_user', views.create_user),
    path('checked_user', views.checked_login),
    path('affirm_invoice', views.affirm_invoice)
]
