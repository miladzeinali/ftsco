# Generated by Django 3.1 on 2020-08-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200807_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cylinderhandler',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='tyrehandler',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
