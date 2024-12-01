# Generated by Django 5.1.1 on 2024-11-24 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naturalworld_d', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='marketplace_rut',
            field=models.CharField(default='96756430', help_text='Rut asociado al Marketplace sin puntos ni dígito verificador. RUT pruebas = 96756430', max_length=15, verbose_name='Marketplace RUT'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='seller_rut',
            field=models.CharField(default='96756430', help_text='Rut asociado al Vendedor sin puntos ni dígito verificador. RUT pruebas = 96756430', max_length=15, verbose_name='Seller RUT'),
        ),
    ]
