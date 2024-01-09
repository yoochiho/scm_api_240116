
from django.urls import path,include
from app_240102 import views,views_table, test_sql

urlpatterns = [
    path('',views.index),
    path('create',views.create),
    path('read/<id>',views.read),
    path('delete',views.delete),
    path('update/<id>',views.update),
    path('raw/',views_table.load_data),
    path('query/',views.query),
    path('queryrun/',views.queryrun)
    
]
