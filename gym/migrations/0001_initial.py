# Generated by Django 5.1.4 on 2024-12-24 15:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duracion_dias', models.IntegerField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'planes',
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_alta', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'socios',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_vencimiento', models.DateTimeField()),
                ('estado', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('PAGADO', 'Pagado'), ('VENCIDO', 'Vencido')], default='PENDIENTE', max_length=10)),
                ('metodo_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('comprobante_nro', models.CharField(blank=True, max_length=50, null=True)),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='gym.socio')),
            ],
            options={
                'db_table': 'pagos',
            },
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('estado', models.CharField(choices=[('ACTIVA', 'Activa'), ('VENCIDA', 'Vencida'), ('CANCELADA', 'Cancelada')], default='ACTIVA', max_length=10)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='membresias', to='gym.plan')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membresias', to='gym.socio')),
            ],
            options={
                'db_table': 'membresias',
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencias', to='gym.socio')),
            ],
            options={
                'db_table': 'asistencias',
            },
        ),
    ]
