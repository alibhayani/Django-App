# Generated by Django 2.0.1 on 2018-02-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PointofSale', '0007_purchasedunits_purchasesalediff_soldunits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
