# Generated by Django 4.2.7 on 2023-11-07 17:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Obra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('localidad', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('dependencia', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('p_inicial', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_gastos', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('proveedor', models.CharField(max_length=255, null=True)),
                ('concepto', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True)),
                ('categoria', models.CharField(choices=[('Administracion', 'Administración'), ('Mano de obra', 'Mano de obra'), ('Materiales', 'Materiales'), ('Viaticos', 'Viáticos'), ('Varios', 'Varios')], max_length=25)),
                ('facturado', models.CharField(choices=[('Facturado', 'Facturado'), ('No Facturado', 'No Facturado')], default='No Facturado', max_length=50)),
                ('Tipo', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia')], default='Efectivo', max_length=50)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Obra.obra')),
            ],
        ),
    ]
