# Generated by Django 2.1.5 on 2020-10-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_processo', '0001_auto_20201019_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planilha',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='processo/'),
        ),
    ]
