# Generated by Django 3.1.4 on 2021-01-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210106_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличе SD карты'),
        ),
    ]
