# Generated by Django 5.1.1 on 2024-11-24 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naturalworld_d', '0003_transportorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportorder',
            name='label_type',
            field=models.CharField(choices=[('0', 'Solo Datos'), ('1', 'EPL Impresora Zebra + Datos'), ('2', 'Imagen en Binario + Datos')], default='2', help_text='Tipo de etiqueta; 0 = Solo Datos, 1 = EPL Zebra + Datos, 2 = Imagen Binaria', max_length=4),
        ),
    ]
