# Generated by Django 5.1.1 on 2024-11-17 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('naturalworld_d', '0008_webhooknotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='order',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='order',
        ),
        migrations.DeleteModel(
            name='WebhookNotification',
        ),
        migrations.DeleteModel(
            name='Shipment',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]