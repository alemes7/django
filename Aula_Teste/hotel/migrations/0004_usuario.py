# Generated by Django 5.0.5 on 2024-05-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_quarto_foto_quarto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]