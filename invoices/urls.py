from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('create_user', views.create_user),
    path('checked_user', views.checked_login)
]
