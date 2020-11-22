# Generated by Django 3.1 on 2020-09-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_auto_20200901_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='plugins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='plugins/')),
            ],
        ),
    ]
