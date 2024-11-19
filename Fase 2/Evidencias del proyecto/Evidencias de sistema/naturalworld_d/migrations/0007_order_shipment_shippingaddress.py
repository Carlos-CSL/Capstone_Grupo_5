# Generated by Django 5.1.1 on 2024-11-17 16:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naturalworld_d', '0006_producto_stock'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_type', models.CharField(max_length=50)),
                ('service_type_code', models.CharField(max_length=50)),
                ('package_type_code', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=100)),
                ('shipping_date', models.DateField()),
                ('tracking_number', models.CharField(blank=True, max_length=100, null=True)),
                ('label_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='naturalworld_d.order')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=10)),
                ('complement', models.CharField(blank=True, max_length=255, null=True)),
                ('commune_code', models.CharField(max_length=10)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='naturalworld_d.order')),
            ],
        ),
    ]