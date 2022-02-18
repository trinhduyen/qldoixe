from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from .views import *
from . import views
urlpatterns = [
  path('', views.index, name='index'),
  path('List_DV/', listDV.as_view(), name='List_DV'),
  path('List_TB/', listTB.as_view(), name='List_TB'),
  path('List_NTB/', listNTB.as_view(), name='List_NTB'),
  path('List_NVT/', listNVT.as_view(), name='List_NVT'),
  path('List_NV/', listNhanVien.as_view(), name='List_NV'),
  path('List_VT/', listVT.as_view(), name='List_VT'),
  path('List_Xe/', XeRaList.as_view(), name='List_Xe'),
  path('List_Xe2/', XeCRaList.as_view(), name='List_Xe2'),
  path('ShowXeRa/<int:pk>', showXeRa.as_view(), name='showXeRa'),
  path('dowloadPDF/<int:pk>', DownloadPDF.as_view(), name='DownloadPDF'),
  path('ViewPDF/<int:pk>', ViewPDF.as_view(), name='ViewPDF'),
  path('listXe/', listXe.as_view(), name='list_Xe'),
  path('bc/', BC.as_view(), name='b_c'),
  
  
]
