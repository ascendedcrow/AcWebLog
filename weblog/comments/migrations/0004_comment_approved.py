# Generated by Django 2.2.10 on 2020-02-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20200214_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]
