# Generated by Django 4.2.7 on 2023-11-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('documento', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('licencia', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.CharField(max_length=50)),
            ],
        ),
    ]