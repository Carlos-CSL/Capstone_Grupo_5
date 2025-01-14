# Generated by Django 5.1.2 on 2024-12-09 19:29

import django.core.validators
import django.db.models.deletion
import naturalworld_d.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Número de teléfono inválido. Debe tener entre 9 y 15 dígitos.', regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254)),
                ('contact_type', models.CharField(choices=[('R', 'Remitente'), ('D', 'Destinatario')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('peso_unitario', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_address_id', models.IntegerField(blank=True, null=True)),
                ('county_coverage_code', models.CharField(max_length=4)),
                ('street_name', models.CharField(max_length=100)),
                ('street_number', models.CharField(blank=True, max_length=10, null=True)),
                ('supplement', models.CharField(blank=True, max_length=255, null=True)),
                ('comuna', models.CharField(default='Desconocido', max_length=100)),
                ('address_type', models.CharField(max_length=4)),
                ('delivery_on_commercial_office', models.BooleanField(default=False)),
                ('commercial_office_id', models.IntegerField(blank=True, null=True)),
                ('observation', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='productos')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('peso', models.DecimalField(decimal_places=2, help_text='Peso en kg', max_digits=5)),
                ('altura', models.IntegerField(help_text='Altura en cm')),
                ('ancho', models.IntegerField(help_text='Ancho en cm')),
                ('largo', models.IntegerField(help_text='Largo en cm')),
                ('tipo_producto', models.CharField(choices=[('tipo1', 'Tipo 1'), ('tipo2', 'Tipo 2')], default='tipo1', max_length=100)),
                ('valor_declarado', models.IntegerField(blank=True, help_text='Valor declarado del producto', null=True)),
                ('stock', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, help_text='Formato: 12345678-9', max_length=12, null=True, validators=[naturalworld_d.models.validar_rut])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, help_text='Formato: +569XXXXXXXX', max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Número de teléfono inválido. Debe tener entre 9 y 15 dígitos.', regex='^\\+?1?\\d{9,15}$')])),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaqueteEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, help_text='Peso en kg', max_digits=10)),
                ('altura', models.IntegerField(help_text='Altura en cm')),
                ('ancho', models.IntegerField(help_text='Ancho en cm')),
                ('largo', models.IntegerField(help_text='Largo en cm')),
                ('servicio_entrega_codigo', models.IntegerField(help_text='Código del servicio de entrega')),
                ('product_code', models.IntegerField(choices=[(1, 'Documento'), (3, 'Encomienda')], help_text='Código del tipo de producto a enviar; 1 = Documento, 3 = Encomienda')),
                ('referencia_envio', models.CharField(help_text='Referencia única para el envío', max_length=150, unique=True)),
                ('referencia_grupo', models.CharField(help_text='Referencia para el grupo de envíos', max_length=150)),
                ('contenido_declarado', models.IntegerField(blank=True, choices=[(1, 'Artículos Personales'), (10000331, 'Celular'), (2, 'Educación'), (4, 'Vestuario'), (5, 'Otros'), (7, 'Tecnología')], help_text='Tipo de producto enviado: 1 = Artículos Personales, 10000331 = Celular, 2 = Educación, 4 = Vestuario, 5 = Otros, 7 = Tecnología', null=True)),
                ('valor_declarado', models.IntegerField(blank=True, help_text='Valor declarado del producto', null=True)),
                ('receivable_amount_in_delivery', models.DecimalField(blank=True, decimal_places=2, help_text='Monto a cobrar, en caso que el cliente tenga habilitada esta opción.', max_digits=10, null=True)),
                ('addresses', models.ManyToManyField(blank=True, related_name='paquetes_envio', to='naturalworld_d.direccion')),
                ('contacts', models.ManyToManyField(blank=True, related_name='paquetes_envio', to='naturalworld_d.contacto')),
            ],
        ),
        migrations.CreateModel(
            name='PaqueteDetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('detalle_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naturalworld_d.detallepedido')),
                ('paquete_envio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naturalworld_d.paqueteenvio')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('numero_orden', models.CharField(blank=True, db_index=True, max_length=20, unique=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('customer_card_number', models.CharField(default='18578680', help_text='Número de Tarjeta Cliente Chilexpress (TCC). TCC pruebas = 18578680', max_length=12, verbose_name='Customer Card Number')),
                ('label_type', models.CharField(choices=[('0', 'Solo Datos'), ('1', 'EPL Impresora Zebra + Datos'), ('2', 'Imagen en Binario + Datos')], default='2', help_text='Tipo de etiqueta; 0 = Solo Datos;1 = EPL Impresora Zebra + Datos;2 = Imagen en Binario + Datos', max_length=4, verbose_name='Label Type')),
                ('county_of_origin_coverage_code', models.CharField(default='PUDA', help_text='Código de cobertura de origen obtenido por la API Consultar Coberturas', max_length=4, verbose_name='County of Origin Coverage Code')),
                ('estado', models.CharField(default='pendiente', max_length=20)),
                ('estado_envio', models.CharField(blank=True, max_length=20, null=True)),
                ('numero_seguimiento', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('servicio_cotizado', models.IntegerField(blank=True, null=True)),
                ('respuesta_envio', models.JSONField(blank=True, null=True)),
                ('certificate_number', models.BigIntegerField(blank=True, help_text='Número de certificado, si no se ingresa se creará uno nuevo', null=True)),
                ('marketplace_rut', models.CharField(default='96756430', help_text='Rut asociado al Marketplace sin puntos ni dígito verificador. RUT pruebas = 96756430', max_length=15, verbose_name='Marketplace RUT')),
                ('seller_rut', models.CharField(default='96756430', help_text='Rut asociado al Vendedor sin puntos ni dígito verificador. RUT pruebas = 96756430', max_length=15, verbose_name='Seller RUT')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='naturalworld_d.cliente')),
                ('direccion', models.ForeignKey(blank=True, help_text='Dirección asociada al pedido', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos', to='naturalworld_d.direccion')),
            ],
        ),
        migrations.AddField(
            model_name='paqueteenvio',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paquetes_envio', to='naturalworld_d.pedido'),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pago', models.CharField(max_length=100, unique=True)),
                ('estado', models.CharField(max_length=50)),
                ('detalle_estado', models.CharField(blank=True, max_length=200, null=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('referencia_externa', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='naturalworld_d.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='EnvioGenerado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_seguimiento', models.CharField(db_index=True, help_text='Número de seguimiento del envío', max_length=100)),
                ('etiqueta', models.FileField(blank=True, help_text='Etiqueta generada por Chilexpress', null=True, upload_to='etiquetas/')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('generado', 'Generado'), ('en_transito', 'En Tránsito'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20)),
                ('fecha_generacion', models.DateTimeField(blank=True, null=True)),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='envio', to='naturalworld_d.pedido')),
            ],
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_pedido', to='naturalworld_d.pedido'),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naturalworld_d.producto'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('visible', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='naturalworld_d.producto')),
            ],
        ),
        migrations.CreateModel(
            name='TransportOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_order_number', models.CharField(help_text='Número de la Orden de Transporte generado por Chilexpress', max_length=20, unique=True)),
                ('certificate_number', models.CharField(help_text='Número del certificado asociado a la orden de transporte', max_length=20)),
                ('count_of_generated_orders', models.IntegerField(help_text='Cantidad de órdenes generadas asociadas a esta operación')),
                ('reference', models.CharField(help_text='Referencia de la orden (ej. número de pedido)', max_length=50)),
                ('barcode', models.CharField(help_text='Código de barras de la orden de transporte', max_length=50)),
                ('classification_data', models.CharField(help_text='Datos de clasificación de la orden', max_length=50)),
                ('label_type', models.CharField(choices=[('0', 'Solo Datos'), ('1', 'EPL Impresora Zebra + Datos'), ('2', 'Imagen en Binario + Datos')], default='2', help_text='Tipo de etiqueta; 0 = Solo Datos, 1 = EPL Zebra + Datos, 2 = Imagen Binaria', max_length=4)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('generado', 'Generado'), ('en_transito', 'En Tránsito'), ('entregado', 'Entregado')], default='pendiente', help_text='Estado actual de la orden de transporte', max_length=20)),
                ('product_description', models.CharField(blank=True, help_text='Descripción del producto asociado a la orden de transporte', max_length=100, null=True)),
                ('service_description', models.CharField(help_text="Descripción del servicio de transporte (ej. 'PRIORITARIO')", max_length=100)),
                ('service_description_full', models.CharField(help_text='Descripción completa del servicio de transporte', max_length=100)),
                ('generic_string1', models.CharField(blank=True, help_text='Campo genérico opcional 1', max_length=50, null=True)),
                ('generic_string2', models.CharField(blank=True, help_text='Campo genérico opcional 2', max_length=50, null=True)),
                ('delivery_type_code', models.CharField(help_text="Código de tipo de entrega (ej. 'EXPRESS', 'PRIORITARIO')", max_length=10)),
                ('destination_coverage_area_name', models.CharField(help_text='Área de cobertura del destino', max_length=100)),
                ('additional_product_description', models.CharField(blank=True, help_text='Descripción adicional del producto asociado', max_length=100, null=True)),
                ('distribution_description', models.CharField(help_text='Descripción de la distribución', max_length=100)),
                ('delivery_zone_id', models.IntegerField(help_text='ID de la zona de entrega')),
                ('company_name', models.CharField(blank=True, help_text='Nombre de la empresa (si aplica)', max_length=100, null=True)),
                ('recipient', models.CharField(help_text='Nombre del destinatario', max_length=100)),
                ('address', models.CharField(help_text='Dirección de entrega', max_length=255)),
                ('group_reference', models.CharField(help_text='Referencia del grupo de envíos (si corresponde)', max_length=50)),
                ('printed_date', models.DateTimeField(help_text='Fecha en que se imprimió la orden')),
                ('created_date', models.DateTimeField(help_text='Fecha de creación de la orden')),
                ('fecha_generacion', models.DateTimeField(auto_now_add=True, help_text='Fecha en que se generó la orden de transporte en el sistema')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, help_text='Última vez que se actualizó la información')),
                ('label_version', models.CharField(help_text='Versión de la etiqueta', max_length=10)),
                ('label_data', models.TextField(blank=True, help_text='Etiqueta en Base64 (si la API la devuelve en este formato)', null=True)),
                ('etiqueta', models.FileField(blank=True, help_text='Etiqueta generada por Chilexpress para el envío', null=True, upload_to='etiquetas/')),
                ('respuesta_api', models.JSONField(blank=True, help_text='Respuesta completa de la API al generar la orden de transporte', null=True)),
                ('pedido', models.OneToOneField(help_text='Pedido asociado a esta orden de transporte', on_delete=django.db.models.deletion.CASCADE, related_name='transport_order', to='naturalworld_d.pedido')),
            ],
        ),
    ]
