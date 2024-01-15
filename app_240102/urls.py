from django.urls import path,include
from app_240102 import views,views_table

urlpatterns = [
    path('',views.index),
    path('create',views.create),
    path('read/<id>',views.read),
    path('delete',views.delete),
    path('update/<id>',views.update),
    path('query/',views.query),
    path('crontab_scm/',views_table.crontab_scm)
    
]
