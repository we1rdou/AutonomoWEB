# Generated by Django 5.0.6 on 2024-05-16 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminRestaurante', '0005_plato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='Cliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='Empleado',
            new_name='empleado',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='Mesa',
            new_name='mesa',
        ),
        migrations.RenameField(
            model_name='plato',
            old_name='Pedido',
            new_name='pedido',
        ),
    ]
