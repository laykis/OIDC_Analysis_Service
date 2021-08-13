# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bpmdata(models.Model):
    bid = models.BigAutoField(db_column='BID', primary_key=True)  # Field name made lowercase.
    tid = models.ForeignKey('Bpmtest', models.DO_NOTHING, db_column='TID')  # Field name made lowercase.
    mid = models.ForeignKey('Movieinfo', models.DO_NOTHING, db_column='MID')  # Field name made lowercase.
    bpm = models.TextField(db_column='BPM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPMDATA'


class Bpmtest(models.Model):
    tid = models.BigAutoField(db_column='TID', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='UID')  # Field name made lowercase.
    mid = models.ForeignKey('Movieinfo', models.DO_NOTHING, db_column='MID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BPMTEST'


class Moviecomment(models.Model):
    cid = models.BigAutoField(db_column='CID', primary_key=True)  # Field name made lowercase.
    mid = models.ForeignKey('Movieinfo', models.DO_NOTHING, db_column='MID')  # Field name made lowercase.
    uid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='UID')  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=255)  # Field name made lowercase.
    deleteyn = models.CharField(db_column='DELETEYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    insert_time = models.DateTimeField(db_column='INSERT_TIME')  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    delete_time = models.DateTimeField(db_column='DELETE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIECOMMENT'


class Moviegraph(models.Model):
    gid = models.BigAutoField(db_column='GID', primary_key=True)  # Field name made lowercase.
    mid = models.ForeignKey('Movieinfo', models.DO_NOTHING, db_column='MID')  # Field name made lowercase.
    bpm = models.IntegerField(db_column='BPM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIEGRAPH'


class Movieinfo(models.Model):
    mid = models.BigAutoField(db_column='MID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100)  # Field name made lowercase.
    bmax = models.IntegerField(db_column='BMAX', blank=True, null=True)  # Field name made lowercase.
    bmin = models.IntegerField(db_column='BMIN', blank=True, null=True)  # Field name made lowercase.
    runningtime = models.IntegerField(db_column='RUNNINGTIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIEINFO'


class Movielove(models.Model):
    lid = models.BigAutoField(db_column='LID', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='UID')  # Field name made lowercase.
    mid = models.ForeignKey(Movieinfo, models.DO_NOTHING, db_column='MID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIELOVE'


class Movierank(models.Model):
    mid = models.ForeignKey(Movieinfo, models.DO_NOTHING, db_column='MID')  # Field name made lowercase.
    rank = models.IntegerField(db_column='RANK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIERANK'


class Scoring(models.Model):
    mid = models.ForeignKey(Movieinfo, models.DO_NOTHING, db_column='MID')  # Field name made lowercase.
    score = models.CharField(db_column='SCORE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCORING'


class Userinfo(models.Model):
    uid = models.BigAutoField(db_column='UID', primary_key=True)  # Field name made lowercase.
    uname = models.CharField(db_column='UNAME', max_length=50)  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=50)  # Field name made lowercase.
    userpw = models.CharField(db_column='USERPW', max_length=50)  # Field name made lowercase.
    usex = models.CharField(db_column='USEX', max_length=2)  # Field name made lowercase.
    useremail = models.CharField(db_column='USEREMAIL', max_length=50)  # Field name made lowercase.
    unumber = models.CharField(db_column='UNUMBER', max_length=15)  # Field name made lowercase.
    uage = models.CharField(db_column='UAGE', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERINFO'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
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
