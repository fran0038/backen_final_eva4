# Generated by Django 4.1.4 on 2022-12-20 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cliente_vendedor_alter_producto_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='apellido',
            field=models.CharField(max_length=50),
        ),
    ]
