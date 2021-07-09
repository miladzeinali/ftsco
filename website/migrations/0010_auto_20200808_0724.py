# Generated by Django 3.1 on 2020-08-08 07:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200807_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrutHandler',
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
                ('sideShift_Mm', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('sideShift_In', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('body_Rotation', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('Handler_tilting', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='struthandler/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('price_Toman', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('price_Dollar', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='cylinderhandler',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tyrehandler',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
