# Generated by Django 2.1.7 on 2019-03-05 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0048_auto_20190301_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodtype',
            name='rebate',
            field=models.PositiveIntegerField(default=0, verbose_name='返利金额'),
        ),
    ]