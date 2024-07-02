# Generated by Django 4.0.4 on 2023-04-29 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0004_alter_courier_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report', models.TextField(null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('report_id', models.CharField(default=uuid.uuid4, max_length=50)),
                ('courier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.courier')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
