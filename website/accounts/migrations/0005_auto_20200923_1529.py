# Generated by Django 2.2.12 on 2020-09-23 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.User'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Opere', 'Opere'), ('Strumenti', 'Strumenti')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
