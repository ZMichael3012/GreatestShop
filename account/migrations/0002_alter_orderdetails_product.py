# Generated by Django 4.0.3 on 2022-03-16 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_product_brand'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='market.product'),
        ),
    ]
