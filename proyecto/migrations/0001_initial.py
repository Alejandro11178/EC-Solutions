# Generated by Django 4.2.1 on 2023-11-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('rol', models.CharField(choices=[('alumno', 'Alumno'), ('profesor', 'Profesor')], max_length=10)),
                ('materia', models.CharField(blank=True, max_length=100, null=True)),
                ('horarios', models.CharField(blank=True, max_length=100, null=True)),
                ('nivel', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
