# Generated by Django 3.2.18 on 2023-08-09 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relation',
            old_name='form_user',
            new_name='from_user',
        ),
    ]