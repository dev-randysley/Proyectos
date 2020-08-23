# Generated by Django 3.1 on 2020-08-20 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='')),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Ultima Actualizacion')),
            ],
        ),
    ]
