# Generated by Django 3.0.5 on 2023-03-05 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0032_auto_20230305_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='tests',
        ),
    ]