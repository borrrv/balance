# Generated by Django 3.2.10 on 2023-04-13 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reserve', '0011_auto_20230413_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='reserve.service', verbose_name='Наименование услуги')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь с услугой')),
            ],
        ),
    ]
