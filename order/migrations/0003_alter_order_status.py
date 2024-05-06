# Generated by Django 5.0.4 on 2024-05-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ND', 'Not Delivered'), ('D', 'Delivered')], max_length=4),
        ),
    ]
