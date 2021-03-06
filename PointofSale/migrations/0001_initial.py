# Generated by Django 2.0.1 on 2018-01-30 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=50)),
                ('Type', models.CharField(choices=[('EQ', 'Equipment'), ('PT', 'Parts'), ('VH', 'Vehicle')], max_length=2)),
                ('Quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Quantity', models.IntegerField()),
                ('Date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PointofSale.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Quantity', models.IntegerField()),
                ('Date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PointofSale.Product')),
            ],
        ),
    ]
