# Generated by Django 4.2.2 on 2023-06-20 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=240)),
                ('rua', models.CharField(max_length=240)),
                ('numero', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Locais',
            },
        ),
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=240)),
                ('data_inicio', models.DateTimeField(null=True)),
                ('data_fim', models.DateTimeField(null=True)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.local')),
            ],
        ),
    ]
