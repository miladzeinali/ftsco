# Generated by Django 3.1 on 2020-08-07 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200807_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tyrehandler',
            old_name='OpeningRangeInMax',
            new_name='OpeningRange_In_Max',
        ),
        migrations.RenameField(
            model_name='tyrehandler',
            old_name='OpeningRangeInMin',
            new_name='OpeningRange_In_Min',
        ),
        migrations.RenameField(
            model_name='tyrehandler',
            old_name='OpeningRangeMmMax',
            new_name='OpeningRange_Mm_Max',
        ),
        migrations.RenameField(
            model_name='tyrehandler',
            old_name='OpeningRangeMmMin',
            new_name='OpeningRange_Mm_Min',
        ),
        migrations.RenameField(
            model_name='tyrehandler',
            old_name='capacityLbs',
            new_name='capacity_Lbs',
        ),
        migrations.RenameField(
            model_name='tyrehandler',
            old_name='sideShiftIn',
            new_name='sideShift_In',
        ),
        migrations.RenameField(
            model_name='tyrehandler',
            old_name='sideShiftMm',
            new_name='sideShift_Mm',
        ),
    ]
