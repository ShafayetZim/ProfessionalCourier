# Generated by Django 3.0.7 on 2022-04-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_set', '0010_auto_20220411_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='payable',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]