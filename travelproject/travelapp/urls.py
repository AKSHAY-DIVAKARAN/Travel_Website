from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),



    # path('',views.demo1,name='demo1')
]






