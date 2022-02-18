from datetime import date
import datetime
import io
from itertools import chain
from unittest import result
from django.shortcuts import render
from .forms import *
from django.views.generic  import TemplateView
from django.views.generic.list import ListView
from .models import *
from django.db.models import Avg, Max, Min, Sum
# Create your views here.
from io import BytesIO, StringIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result= BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('utf-8')), result)
  #  pdf = pisa.pisaDocument(BytesIO(html.encoding('utf8')),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
     
    return None

class ViewPDF(View):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        data = VatTuDung.objects.filter(XeVao_id = pk)
        vt = material.objects.all()
        dt = XeVao.objects.filter(id =pk)
        date = datetime.datetime.now()
        sum= VatTuDung.objects.filter(XeVao_id = pk).aggregate(total=Sum('thanhtien'))['total']
        data ={'data':data, 'date':date,'dt':dt, 'sum':sum, 'vt':vt}
        pdf = render_to_pdf('PDF/VT.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
  
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        data = VatTuDung.objects.filter(XeVao_id = pk)
        vt = material.objects.all()
        dt = XeVao.objects.filter(id =pk)
        date = datetime.datetime.now()
        sum= VatTuDung.objects.filter(XeVao_id = pk).aggregate(total=Sum('thanhtien'))['total']
        data ={'data':data, 'date':date,'dt':dt, 'sum':sum, 'vt':vt}
        pdf = render_to_pdf('PDF/VT.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "vt%s.pdf" %("12341231")
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response


def index(request):
    return render(request, 'base.html')


class listDV(ListView):
    model= dv
    template_name= 'DV/index.html'
    context_object_name ='dv'
    paginate_by = 4

class listTB(ListView):
    model = thietbi
    template_name ='ThietBi/index.html'
    context_object_name ='TB'
    paginate_by = 4
    def get_queryset(self, **args) :
        queryset= super().get_queryset()
        qry = 'select a."NameTB",a."id" ,b."NameGroupTB" from "DX_thietbi" a , "DX_groupthietbi" b where a."id" = b."id"  '
        queryset = thietbi.objects.raw(qry)
        return queryset
    
class listNTB(ListView):
    model= groupthietbi
    template_name= 'NhomTB/index.html'
    context_object_name ='NTB'
    paginate_by = 4


class listNVT(ListView):
    model = groupmaterial
    template_name = 'NVT/index.html'
    context_object_name ='NVT'
    paginate_by =10
  
class listNhanVien(ListView):
    model = NhanVien
    template_name = 'NhanVien/index.html'
    context_object_name ='NV'
    paginate_by =10    
      
class listXe(ListView):
    model = Xe
    template_name = 'Xe/index.html'
    context_object_name ='Xe'
    paginate_by =10   

class listVT(ListView):
    template_name = 'VatTu/index.html'
    context_object_name ='VT'
    model = material
    paginate_by = 10
    def  get_queryset(self,**args):
        queryset=super().get_queryset()
        qry =' select a."id" ,a."IdVT",a."NameVT",b."NameNVT",c."NameDv" from "DX_material" a ,"DX_groupmaterial" b ,"DX_dv" c where a."IdNVTF_id" = b."id" and a."IdDV_id"= c."id"  '
        queryset= material.objects.raw(qry)
        return queryset

class  XeRaList(ListView):
    model= XeVao
    template_name ='chitietxe/index.html'
    context_object_name= 'XV'
    paginate_by =10
    def get_queryset(self,**args):
        queryset= super().get_queryset()
        qry ='select * from "DX_xevao" where "datetimeXera" is not null'
        queryset= XeVao.objects.raw(qry)
        return queryset


class  XeCRaList(ListView):
    model= XeVao
    template_name ='chitietxe/index.html'
    context_object_name= 'XV'
    paginate_by =10
    def get_queryset(self,**args):
        queryset= super().get_queryset()
        qry ='select * from "DX_xevao" where "datetimeXera" is  null'
        queryset= XeVao.objects.raw(qry)
        return queryset


   
class showXeRa(ListView):
    model=VatTuDung
    template_name = 'chitietxe/ShowXeRa.html'
    context_object_name = 'XR'
    paginate_by = 10
    def get_queryset(self,**kwargs):
        queryset= super().get_queryset()
        pk= self.kwargs['pk']
        qry= 'select a.*,d.*,e.*,c."NameVT",c."IdDV_id",f."NameDv", b.* from "DX_vattudung" a ,"DX_dv" f, "DX_xevao" b ,"DX_material" c ,"DX_xe" d,"DX_nhanvien" e where c."IdDV_id"=f."id" and d."id"= b."BienSoXe_id" and e."id" = b."NhanVienPT_id" and a."VtSudung_id"=c."id" and  a."XeVao_id" = b."id" and a."XeVao_id"= %d '%pk
        queryset = VatTuDung.objects.raw(qry)
        return queryset
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)   
        pk= self.kwargs['pk']
        vt = VatTuDung.objects.filter(XeVao_id = pk)
        context['count'] = vt.count()
        context['xe']= XeVao.objects.filter(id=pk)
        context['date'] = datetime.datetime.now()
        context['sum'] = self.model.objects.filter(XeVao_id = pk).aggregate(total=Sum('thanhtien'))['total']
        return context
    

class BC (ListView):
    template_name = 'BC/index.html'
    context_object_name ='bc'
    model= VatTuDung
    def get_queryset(self,**kwargs):
        queryset= super().get_queryset()
        qry= 'select a."NameVT",a."id", sum(b."thanhtien") as tt from "DX_material" a, "DX_vattudung" b group by a."NameVT",a."id"'
        qry1 = 'select "BienSoXe" as id, sum(tt) as sum from (select a."id", c."BienSoXe", sum(b."thanhtien") as tt  from "DX_xevao" a, "DX_vattudung" b,"DX_xe" c where c."id"= a."BienSoXe_id" and a."id" = b."XeVao_id" group by c."BienSoXe",a."id") as a group by "BienSoXe"'
        queryset = {
          'one' :  VatTuDung.objects.raw(qry),
          'two' :VatTuDung.objects.raw(qry1)
        }
        return queryset
           