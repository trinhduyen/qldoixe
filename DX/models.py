from asyncio.windows_events import NULL
from datetime import timezone
from email.policy import default
from typing import Callable
from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from django.db.models.enums import TextChoices

class groupmaterial(models.Model):
    NameNVT = models.CharField(max_length=255, unique=True)
   
    def __str__(seft):
        return seft.NameNVT
    
class dv(models.Model):  
    NameDv= models.CharField(max_length = 255, unique=True)
   
    def __str__(seft):
            return seft.NameDv
    
class material(models.Model):
    IdVT = models.CharField(unique=True,max_length=255)   
    NameVT = models.CharField(max_length=255, unique=True)
    IdNVTF = models.ForeignKey(groupmaterial,on_delete = models.SET_NULL,null=True) 
    IdDV = models.ForeignKey(dv, on_delete =  models.SET_NULL,null=True)
   
    def __str__(self):
        return self.NameVT


    
class groupthietbi(models.Model):
    NameGroupTB = models.CharField(max_length=255, unique=True)    
    
    def __str__(seft):
        return seft.NameGroupTB

class thietbi(models.Model):
    IdGroupTB= models.ForeignKey(groupthietbi, on_delete= models.SET_NULL,null=True)    
    NameTB = models.CharField(max_length=255, unique=True)
    
    def __str__(seft):
        return seft.NameTB

    
class Xe(models.Model):
    BienSoXe = models.CharField(max_length=255)
   
    def __str__(self):
        return self.BienSoXe
    
    
class NhanVien(models.Model):
    MaNV = models.CharField(max_length=255, unique=True)
    TenNV = models.CharField(max_length=255)
    TuoiNV= models.IntegerField()
    Namlv= models.IntegerField()
    
    def __str__(sefl):
        return sefl.TenNV
        
trangthaikho = {
    ("Có", "Có"),
    ("Không", "Không")
}    
    
trangthaixuat={
    ("Đã Xuất", "Đã Xuất"),
    ("Chưa Xuất", "Chưa Xuất")
} 

class XeVao(models.Model):
    sophieu = models.UUIDField(default=uuid.uuid4)
    datetimeXevao= models.DateTimeField()
    Status =models.BooleanField(default=False)
    datetimeXera = models.DateTimeField(blank=True, null=True)
    BienSoXe = models.ForeignKey(Xe,on_delete= models.SET_NULL,null=True)
    NhanVienPT = models.ForeignKey(NhanVien,on_delete=  models.SET_NULL,null=True)
    LyDoXeVao  = models.TextField(max_length=500)
    Lydo = models.TextField(max_length=500)
 
    def __str__(self):
       return str(self.sophieu)
   
        

class VatTuDung(models.Model):
    XeVao= models.ForeignKey(XeVao, on_delete= models.SET_NULL,null=True)
    VtSudung = models.ForeignKey(material, on_delete= models.SET_NULL,null=True)  
    dongia= models.FloatField()
    SoLuong = models.PositiveIntegerField()
    thanhtien = models.FloatField()
    TrangThaiKho = models.CharField(choices=trangthaikho , max_length=50)    
    TrangThaiXuat = models.CharField(choices=trangthaixuat, max_length=50)   
    DatetimeXuat = models.DateTimeField(blank=True, null=True )
   
 
