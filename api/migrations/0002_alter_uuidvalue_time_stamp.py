# Generated by Django 3.2.5 on 2022-01-14 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uuidvalue',
            name='time_stamp',
            field=models.CharField(max_length=50),
        ),
    ]
