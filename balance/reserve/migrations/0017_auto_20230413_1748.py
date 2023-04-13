# Generated by Django 3.2.10 on 2023-04-13 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reserve', '0016_auto_20230413_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL, verbose_name='Владелец заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='reserve.service', verbose_name='Услуга'),
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revenue', to='reserve.order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revenue', to='reserve.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revenue', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserve', to='reserve.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserve', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
