# Generated by Django 3.1.2 on 2020-10-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0004_auto_20201021_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barcode',
            name='barcode_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
