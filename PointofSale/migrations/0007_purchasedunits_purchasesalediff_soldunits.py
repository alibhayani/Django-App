# Generated by Django 2.0.1 on 2018-02-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PointofSale', '0006_auto_20180201_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasedUnits',
            fields=[
                ('Product_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Total_Units', models.IntegerField()),
            ],
            options={
                'db_table': 'units_purchased',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseSaleDiff',
            fields=[
                ('Product_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Difference', models.IntegerField()),
            ],
            options={
                'db_table': 'Purchase_Sale_Diff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SoldUnits',
            fields=[
                ('Product_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Total_Units', models.IntegerField()),
            ],
            options={
                'db_table': 'units_sold',
                'managed': False,
            },
        ),
    ]
