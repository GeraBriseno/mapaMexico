# Generated by Django 4.1.1 on 2022-10-27 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa1', '0003_alter_pib_a2003_alter_pib_a2004_alter_pib_a2005_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Densidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50, verbose_name='estado')),
                ('a1990', models.FloatField(verbose_name='1990')),
                ('a1995', models.FloatField(verbose_name='1995')),
                ('a2000', models.FloatField(verbose_name='2000')),
                ('a2005', models.FloatField(verbose_name='2005')),
                ('a2010', models.FloatField(verbose_name='2010')),
                ('a2015', models.FloatField(verbose_name='2015')),
                ('a2020', models.FloatField(verbose_name='2020')),
            ],
        ),
    ]
