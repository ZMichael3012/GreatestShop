# Generated by Django 4.0.3 on 2022-03-15 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Man'), ('F', 'Woman'), ('N', 'None')], max_length=1)),
                ('category', models.CharField(choices=[('Hoodie', 'Hoodie'), ('Accessories', 'Accessories'), ('Pants', 'Pants')], max_length=15)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='market.brand')),
            ],
        ),
    ]
