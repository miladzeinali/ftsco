# Generated by Django 3.1 on 2020-08-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_productimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='milad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='mm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erer', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
    ]
