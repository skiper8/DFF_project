# Generated by Django 4.2.3 on 2023-08-04 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_alter_subscribetocourse_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribetocourse',
            name='subscribe_status',
            field=models.BooleanField(default=True, verbose_name='статус подписки'),
        ),
    ]
