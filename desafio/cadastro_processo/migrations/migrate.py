from django.db import migrations, models

class Migration(migrations.Migration):
    
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name = 'Processos',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=100)),
                ('arquivo', models.CharField(max_length=100)),
            ],
        ),
    ]