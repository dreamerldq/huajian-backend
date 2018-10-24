from django.urls import path

from . import views
urlpatterns = [

    path('create_expend', views.create_expend),
    path('delete_expend', views.delete_expend),
    path('expend_list', views.expend_list),
    path('update_expend_state', views.update_expend_state),
]
