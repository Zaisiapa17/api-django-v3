# Generated by Django 5.0.1 on 2024-02-01 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCustomer', '0006_alter_customer_table_alter_ordercontainer_table'),
        ('appProduct', '0003_alter_category_table_alter_product_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordercontainer',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='ordercontainer',
            old_name='product_id',
            new_name='product',
        ),
        migrations.AlterUniqueTogether(
            name='ordercontainer',
            unique_together={('customer', 'product')},
        ),
    ]