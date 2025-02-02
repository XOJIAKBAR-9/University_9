# Generated by Django 5.1.1 on 2024-09-17 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('asosiy', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=10)),
                ('yosh', models.PositiveIntegerField(blank=True)),
                ('daraja', models.CharField(choices=[('Bakalavr', 'Bakalavr'), ('Magsitr', 'Magsitr'), ('Aspirant', 'Aspirant'), ('Dokotrant', 'Dokotrant')], max_length=50)),
                ('fan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Uniapp.fan')),
            ],
        ),
        migrations.AddField(
            model_name='fan',
            name='yonalish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Uniapp.yonalish'),
        ),
    ]
