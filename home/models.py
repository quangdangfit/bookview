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
    ma_ht = models.IntegerField(primary_key=True)
    ten_ht = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ten_ht


class Loai(models.Model):
    ma_loai = models.IntegerField(primary_key=True)
    ten_loai = models.CharField(max_length=45)
    mo_ta = models.TextField(blank=True, null=True)
    cha = models.ForeignKey('self', models.DO_NOTHING, db_column='cha', blank=True, null=True)

    def __str__(self):
        return self.ten_loai


class LoaiSach(models.Model):
    id = models.IntegerField(primary_key=True)
    ma_sach = models.ForeignKey('Sach', models.DO_NOTHING, db_column='ma_sach')
    ma_loai = models.ForeignKey(Loai, models.DO_NOTHING, db_column='ma_loai')

    def __str__(self):
        return str(self.ma_sach) + ' - ' + str(self.ma_loai)


class NgonNgu(models.Model):
    ma_nn = models.IntegerField(primary_key=True)
    ten_nn = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ten_nn


class Sach(models.Model):
    ma_sach = models.IntegerField(primary_key=True)
    ten_sach = models.CharField(max_length=150)
    bia_sach = models.ImageField(null=True)
    isbn = models.CharField(max_length=15)
    so_trang = models.IntegerField(blank=True, null=True)
    namxb = models.TextField(blank=True, null=True)  # This field type is a guess.
    hinh_thuc = models.ForeignKey(HinhThuc, models.DO_NOTHING, db_column='hinh_thuc', blank=True, null=True)
    ngon_ngu = models.ForeignKey(NgonNgu, models.DO_NOTHING, db_column='ngon_ngu', blank=True, null=True)
    mo_ta = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ten_sach


class TacGia(models.Model):
    ma_tg = models.IntegerField(primary_key=True)
    ten_tg = models.CharField(max_length=100)
    hinh = models.ImageField(null=True)
    nam_sinh = models.TextField(blank=True, null=True)  # This field type is a guess.
    que_quan = models.CharField(max_length=150, blank=True, null=True)
    mo_ta = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ten_tg


class TacGiaSach(models.Model):
    id = models.IntegerField(primary_key=True)
    ma_sach = models.ForeignKey(Sach, models.DO_NOTHING, db_column='ma_sach')
    ma_tg = models.ForeignKey(TacGia, models.DO_NOTHING, db_column='ma_tg')

    def __str__(self):
        return str(self.ma_sach) + ' - ' + str(self.ma_tg)


class TacGiaTheLoai(models.Model):
    id = models.IntegerField(primary_key=True)
    ma_tg = models.ForeignKey(TacGia, models.DO_NOTHING, db_column='ma_tg', blank=True, null=True)
    ma_loai = models.ForeignKey(Loai, models.DO_NOTHING, db_column='ma_loai', blank=True, null=True)

    def __str__(self):
        return str(self.ma_tg) + ' - ' + str(self.ma_loai)


class NhanXet(models.Model):
    sach = models.ForeignKey(Sach, on_delete=models.CASCADE, db_column='sach', related_name='nhan_xet', null=True)
    tac_gia = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='tac_gia', on_delete=models.CASCADE)
    noi_dung = models.TextField(null=True)
    ngay_dang = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.noi_dung
