# Generated by Django 4.2.7 on 2023-11-13 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.TextField(choices=[('', ''), ('Alumno', 'Alumno'), ('Profesor', 'Profesor')], default='', max_length=8, verbose_name='rol'),
        ),
    ]