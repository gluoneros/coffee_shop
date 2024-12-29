# Generated by Django 5.1.4 on 2024-12-29 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='nombre')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='precio')),
                ('description', models.TextField(max_length=300, verbose_name='descripción')),
                ('available', models.BooleanField(default=True, verbose_name='disponible')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='foto')),
            ],
        ),
    ]
