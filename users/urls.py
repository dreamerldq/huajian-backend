from django.urls import path

from . import views
urlpatterns = [
    path('create_user', views.create_user),
    path('delete_user', views.delete_user),
    path('edit_user', views.edit_user),
    path('get_user', views.get_user),
]
