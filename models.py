# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HomeHinhthuc(models.Model):
    ma_ht = models.AutoField(primary_key=True)
    ten_ht = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_hinhthuc'


class HomeLoai(models.Model):
    ma_loai = models.AutoField(primary_key=True)
    ten_loai = models.CharField(max_length=45)
    mo_ta = models.TextField(blank=True, null=True)
    cha = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_loai'


class HomeLoaisach(models.Model):
    ma_loai = models.IntegerField()
    ma_sach = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'home_loaisach'


class HomeNgonngu(models.Model):
    ma_nn = models.AutoField(primary_key=True)
    ten_nn = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_ngonngu'


class HomeNhanxet(models.Model):
    noi_dung = models.TextField(blank=True, null=True)
    ngay_dang = models.DateField()
    tac_gia = models.IntegerField()
    sach = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_nhanxet'


class HomeSach(models.Model):
    ma_sach = models.AutoField(primary_key=True)
    ten_sach = models.CharField(max_length=150)
    isbn = models.CharField(max_length=15)
    so_trang = models.IntegerField(blank=True, null=True)
    namxb = models.TextField(blank=True, null=True)
    hinh_thuc = models.IntegerField()
    ngon_ngu = models.IntegerField(blank=True, null=True)
    bia_sach = models.CharField(max_length=100, blank=True, null=True)
    mo_ta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_sach'


class HomeTacgia(models.Model):
    ma_tg = models.AutoField(primary_key=True)
    ten_tg = models.CharField(max_length=100)
    nam_sinh = models.TextField(blank=True, null=True)
    que_quan = models.CharField(max_length=150, blank=True, null=True)
    mo_ta = models.TextField(blank=True, null=True)
    hinh = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_tacgia'


class HomeTacgiasach(models.Model):
    ma_sach = models.IntegerField()
    ma_tg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'home_tacgiasach'


class HomeTacgiatheloai(models.Model):
    ma_loai = models.IntegerField(blank=True, null=True)
    ma_tg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_tacgiatheloai'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.PositiveSmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)
