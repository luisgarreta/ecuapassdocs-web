# Generated by Django 4.2.7 on 2023-11-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tipoId', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
    ]
