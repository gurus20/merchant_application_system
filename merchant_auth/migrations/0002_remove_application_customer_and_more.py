# Generated by Django 5.0 on 2024-03-17 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='application',
        ),
        migrations.AddField(
            model_name='application',
            name='merchant',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='merchant_auth.merchant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='application',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='merchant_auth.application'),
            preserve_default=False,
        ),
    ]
