# Generated by Django 4.2.2 on 2023-06-20 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convidado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=240)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='compromisso',
            name='pessoa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agenda.convidado'),
            preserve_default=False,
        ),
    ]