# Generated by Django 5.1.7 on 2025-03-29 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_otpcode_alter_authorprofile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='otpcode',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
    ]
