# Generated by Django 3.0.3 on 2020-03-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200326_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
