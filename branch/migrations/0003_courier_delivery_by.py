# Generated by Django 4.0.4 on 2023-04-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_remove_branch_worker_branch_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='delivery_by',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]