# Generated by Django 5.1.1 on 2024-11-12 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naturalworld_d', '0005_producto_tipo_producto_producto_valor_declarado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
