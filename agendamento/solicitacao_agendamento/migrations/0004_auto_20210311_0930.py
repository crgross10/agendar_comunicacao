# Generated by Django 3.1.7 on 2021-03-11 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao_agendamento', '0003_comunicado_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comunicado',
            old_name='status',
            new_name='status_envio',
        ),
    ]
