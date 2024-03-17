# Generated by Django 5.0 on 2024-03-16 15:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_id', models.CharField(max_length=64)),
                ('application_name', models.CharField(max_length=64)),
                ('website_url', models.URLField(max_length=64)),
                ('secret', models.CharField(max_length=64)),
                ('is_active', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant_auth.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('phone_country_code', models.CharField(max_length=10)),
                ('phone_verified', models.BooleanField(default=False)),
                ('support_email', models.EmailField(max_length=254)),
                ('email_verified', models.BooleanField(default=False)),
                ('merchant_id', models.CharField(max_length=32)),
                ('merchant_name', models.CharField(max_length=16)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant_auth.application')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='merchant_auth.role')),
            ],
        ),
    ]
