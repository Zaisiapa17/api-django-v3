# Generated by Django 5.0.1 on 2024-02-01 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCustomer', '0004_alter_ordercontainer_table_delete_testing'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customers',
        ),
        migrations.AlterModelTable(
            name='ordercontainer',
            table='order_containers',
        ),
    ]
