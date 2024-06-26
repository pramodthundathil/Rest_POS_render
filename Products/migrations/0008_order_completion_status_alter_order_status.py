# Generated by Django 5.0.6 on 2024-06-01 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_order_take_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completion_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('In Kitchen', 'In Kitchen'), ('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
