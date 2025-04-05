# Generated by Django 5.1.7 on 2025-03-22 02:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='authorprofile',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='sellerprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='sellerprofile',
            name='business_phone',
        ),
        migrations.RemoveField(
            model_name='sellerprofile',
            name='full_name',
        ),
        migrations.AddField(
            model_name='authorprofile',
            name='first_name',
            field=models.CharField(max_length=255, null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='authorprofile',
            name='last_name',
            field=models.CharField(max_length=255, null=True, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='first_name',
            field=models.CharField(max_length=255, null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='last_name',
            field=models.CharField(max_length=255, null=True, verbose_name='last name'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='last name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
