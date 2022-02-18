from django.contrib import admin
from . models import *
from .forms import *
# Register your models here.


class VTDAdmin(admin.TabularInline):
    model = VatTuDung
    form = F_VatTuDung
    
class XeVaoAdmin(admin.ModelAdmin):
    list_display =('sophieu','datetimeXevao','datetimeXera',
                   'BienSoXe','NhanVienPT','LyDoXeVao','Lydo')
    list_filter=('BienSoXe','datetimeXevao')
    search_fields=('sophieu','BienSoXe__BienSoXe','NhanVienPT__TenNV','LyDoXeVao')
    inlines=[VTDAdmin,]
    form =F_XeVao
class XeAdmin(admin.ModelAdmin):
    list_display =('id','BienSoXe')
    list_filter=('BienSoXe',)
    search_fields=('id','BienSoXe')
    
class NhanVienAdmin(admin.ModelAdmin):
    list_display =('MaNV','TenNV','TuoiNV','Namlv')
    search_fields=('MaNV','TenNV')    
    
class VatTuDungAdmin(admin.ModelAdmin):
    list_display =('XeVao_id','VtSudung_id','dongia','SoLuong','thanhtien','TrangThaiKho','TrangThaiXuat','DatetimeXuat')
    search_fields=('XeVao__id',)       
    form = F_VatTuDung
class thietbiAdmin(admin.ModelAdmin):
    list_display =('id','IdGroupTB','NameTB')
    search_fields=('NameTB',) 
    form= F_TB

class dvAdmin(admin.ModelAdmin):
    list_display =('id','NameDv')
    search_fields=('NameDv',) 
    form= F_DV    

class materialAdmin(admin.ModelAdmin):
   
    list_display =('IdVT','NameVT','IdNVTF','IdDV')
    search_fields=('NameVT',)
    form = F_Me
    
admin.site.register(NhanVien,NhanVienAdmin)
admin.site.register(Xe,XeAdmin)
admin.site.register(VatTuDung,VatTuDungAdmin)
admin.site.register(XeVao,XeVaoAdmin)
admin.site.register(dv,dvAdmin)
admin.site.register(thietbi,thietbiAdmin)
admin.site.register(groupthietbi)
admin.site.register(groupmaterial)
admin.site.register(material,materialAdmin)

