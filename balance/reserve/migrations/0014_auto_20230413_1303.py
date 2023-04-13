# Generated by Django 3.2.10 on 2023-04-13 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0013_auto_20230413_1221'),
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
