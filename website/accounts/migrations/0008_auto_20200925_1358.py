# Generated by Django 2.2.12 on 2020-09-25 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200923_1541'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
    ]