# Generated by Django 5.0.1 on 2024-02-01 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCustomer', '0003_testing'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ordercontainer',
            table='order_container',
        ),
        migrations.DeleteModel(
            name='Testing',
        ),
    ]