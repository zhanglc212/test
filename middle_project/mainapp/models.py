# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, )
    address = models.CharField(max_length=40)
    potal = models.CharField(max_length=40, )
    phone = models.CharField(max_length=40)
    mobile = models.CharField(max_length=40, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_address'


class TBook(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=40, blank=True, null=True)
    market_price = models.FloatField(blank=True, null=True)
    dang_price = models.FloatField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=40, blank=True, null=True)
    publishing = models.CharField(max_length=40, blank=True, null=True)
    publish_time = models.DateField(blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    impression = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    num = models.IntegerField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    format = models.CharField(max_length=20, blank=True, null=True)
    paper = models.CharField(max_length=20, blank=True, null=True)
    packging = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=120, blank=True, null=True)
    a_intro = models.CharField(max_length=60, blank=True, null=True)
    category = models.ForeignKey('TCategory', models.DO_NOTHING, blank=True, null=True)
    catelog = models.CharField(max_length=40, blank=True, null=True)
    discuss = models.CharField(max_length=40, blank=True, null=True)
    insert_pic = models.CharField(max_length=40, blank=True, null=True)
    book_pic = models.CharField(max_length=40, blank=True, null=True)
    putaway = models.DateTimeField(blank=True, null=True)
    market = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=40, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_category'


class TConfirmString(models.Model):
    ucode = models.CharField(max_length=40,default=None)
    user = models.ForeignKey('TUser', on_delete=models.CASCADE,db_column='user_id')
    code_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 't_confirm_string'


class TOrder(models.Model):
    address = models.ForeignKey('TAddress', models.CASCADE)
    order_num = models.CharField(max_length=40, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('TUser', models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TOrderitem(models.Model):
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    sub_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_orderitem'


class TUser(models.Model):
    email = models.CharField(max_length=60, blank=True, null=True)
    username = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=40, default='0')
    log_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 't_user'
