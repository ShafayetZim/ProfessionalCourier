# Generated by Django 3.2.9 on 2022-02-03 06:56

import data_set.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_set.district')),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('s_village', models.CharField(max_length=100)),
                ('s_phone', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('r_company', models.CharField(blank=True, max_length=100, null=True)),
                ('r_village', models.CharField(max_length=100)),
                ('r_phone', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('order_no', models.CharField(default=data_set.models.order_no_generate, max_length=200, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('tracking', models.CharField(choices=[('1', 'Picked'), ('2', 'In Transit'), ('3', 'Shipped'), ('4', 'Out For Delivery'), ('5', 'Delivered')], default=1, max_length=20)),
                ('status', models.CharField(default='Open', max_length=20)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dis2', to='data_set.district')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dis1', to='data_set.district')),
                ('div', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='div2', to='data_set.division')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='div1', to='data_set.division')),
                ('sub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub1', to='data_set.sub')),
                ('tha', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub2', to='data_set.sub')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_set.type')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_set.division'),
        ),
    ]
