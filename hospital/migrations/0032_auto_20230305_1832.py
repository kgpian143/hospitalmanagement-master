# Generated by Django 3.0.5 on 2023-03-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0031_auto_20230305_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='prescription',
        ),
        migrations.AlterField(
            model_name='patient',
            name='tests',
            field=models.CharField(default='--', max_length=100),
        ),
    ]
