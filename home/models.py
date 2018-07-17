# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings


class HinhThuc(models.Model):
    ma_ht = models.AutoField(primary_key=True)
    ten_ht = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ten_ht


class Loai(models.Model):
    ma_loai = models.AutoField(primary_key=True)
    ten_loai = models.CharField(max_length=45)
    mo_ta = models.TextField(blank=True, null=True)
    cha = models.ForeignKey('self', models.DO_NOTHING, db_column='cha', blank=True, null=True)

    def __str__(self):
        return self.ten_loai


class NgonNgu(models.Model):
    ma_nn = models.AutoField(primary_key=True)
    ten_nn = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ten_nn


class TacGia(models.Model):
    ma_tg = models.AutoField(primary_key=True)
    ten_tg = models.CharField(max_length=100)
    hinh = models.ImageField(null=True)
    nam_sinh = models.IntegerField(default=0)
    que_quan = models.CharField(max_length=150, blank=True, null=True)
    the_loai = models.ManyToManyField(Loai)
    mo_ta = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ten_tg


class PhienBan(models.Model):
    ma_pb = models.AutoField(primary_key=True)
    ten_pb = models.CharField(max_length=150)

    def __str__(self):
        return self.ten_pb


class Sach(models.Model):
    ma_sach = models.AutoField(primary_key=True)
    ten_sach = models.CharField(max_length=150)
    bia_sach = models.ImageField(null=True)
    isbn = models.CharField(max_length=15)
    so_trang = models.IntegerField(blank=True, null=True)
    namxb = models.IntegerField(default=0)
    hinh_thuc = models.ForeignKey(HinhThuc, models.DO_NOTHING, db_column='hinh_thuc', blank=True, null=True)
    ngon_ngu = models.ForeignKey(NgonNgu, models.DO_NOTHING, db_column='ngon_ngu', blank=True, null=True)
    tac_gia = models.ManyToManyField(TacGia)
    the_loai = models.ManyToManyField(Loai)
    phien_ban = models.ForeignKey(PhienBan, models.DO_NOTHING, db_column='phien_ban', blank=True, null=True)
    mo_ta = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ten_sach


class NhanXet(models.Model):
    sach = models.ForeignKey(Sach, on_delete=models.CASCADE, db_column='sach', related_name='nhan_xet', null=True)
    tac_gia = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='tac_gia', on_delete=models.CASCADE)
    noi_dung = models.TextField(null=True)
    ngay_dang = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.noi_dung
