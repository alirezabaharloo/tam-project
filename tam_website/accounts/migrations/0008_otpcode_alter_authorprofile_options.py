# Generated by Django 5.1.7 on 2025-03-29 03:29

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_user_user_type_user_is_author_user_is_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('code', models.CharField(max_length=5)),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='authorprofile',
            options={'verbose_name': 'Author Profile', 'verbose_name_plural': 'Seller Profiles'},
        ),
    ]
