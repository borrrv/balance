# Generated by Django 3.2.10 on 2023-04-13 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0010_auto_20230413_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='service',
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='reserve.service'),
            preserve_default=False,
        ),
    ]
