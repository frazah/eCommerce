# Generated by Django 2.2.12 on 2020-09-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200923_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('In elaborazione', 'In elaborazione'), ('Spedito', 'Spedito'), ('Consegnato', 'Consegnato')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('description', models.CharField(max_length=30, null=True)),
                ('category', models.CharField(choices=[('Disegno', 'Disegno'), ('Acquerelli', 'Acquerelli'), ('Pittura ad olio', 'Pittura ad olio'), ('Scultura', 'Scultura')], max_length=30, null=True)),
            ],
        ),
    ]
