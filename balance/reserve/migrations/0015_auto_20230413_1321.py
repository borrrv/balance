# Generated by Django 3.2.10 on 2023-04-13 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0014_auto_20230413_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='reserve.order', verbose_name='Пользователь с услугой')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='reserve.service', verbose_name='Наименование услуги')),
            ],
        ),
        migrations.DeleteModel(
            name='ServiceUser',
        ),
    ]
