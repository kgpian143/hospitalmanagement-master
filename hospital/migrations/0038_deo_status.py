# Generated by Django 3.0.5 on 2023-03-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0037_deo'),
    ]

    operations = [
        migrations.AddField(
            model_name='deo',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
