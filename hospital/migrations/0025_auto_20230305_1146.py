# Generated by Django 3.0.5 on 2023-03-05 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0024_auto_20230304_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='prescription',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tests',
            field=models.CharField(default='', max_length=100),
        ),
    ]
