# Generated by Django 2.1.5 on 2020-10-19 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_processo', '0003_auto_20201019_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planilha',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='processo/csv/'),
        ),
    ]