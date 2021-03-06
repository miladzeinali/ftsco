# Generated by Django 3.0.7 on 2020-08-31 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_auto_20200820_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='CableHandler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('code', models.CharField(blank=True, max_length=15, null=True)),
                ('model_Year', models.CharField(blank=True, max_length=6, null=True)),
                ('capacity_Kg', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('capacity_Lbs', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('Roll_Diameter_mm', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('Roll_Diameter_in', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cablehandler/')),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('price_Toman', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('price_Dollar', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.category')),
            ],
        ),
        migrations.CreateModel(
            name='RodHandler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('code', models.CharField(blank=True, max_length=15, null=True)),
                ('model_Year', models.CharField(blank=True, max_length=6, null=True)),
                ('capacity_Kg', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('capacity_Lbs', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('Cylinder_Diameter_mm_min', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('Cylinder_Diameter_mm_max', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('Cylinder_Diameter_in_min', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('Cylinder_Diameter_in_max', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('range_daimeter', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='rodhandler/')),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('price_Toman', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('price_Dollar', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.category')),
            ],
        ),
        migrations.CreateModel(
            name='RodHandlerImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='rodhandlerImagesProduct/')),
                ('rodhandler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.RodHandler')),
            ],
        ),
        migrations.CreateModel(
            name='CableHandlerImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cablehandlerImagesProduct/')),
                ('cablehandler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.CableHandler')),
            ],
        ),
    ]
