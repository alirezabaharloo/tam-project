# Generated by Django 5.1.7 on 2025-03-30 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_otpcode_is_valid_alter_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otpcode',
            name='is_valid',
        ),
    ]
