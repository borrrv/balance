# Generated by Django 3.2.10 on 2023-04-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='balance',
            field=models.PositiveIntegerField(default=1, help_text='Баланс пользователя'),
            preserve_default=False,
        ),
    ]
