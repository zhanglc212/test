# Generated by Django 2.0.6 on 2019-05-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190525_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tconfirmstring',
            name='ucode',
            field=models.CharField(default=None, max_length=40),
        ),
    ]