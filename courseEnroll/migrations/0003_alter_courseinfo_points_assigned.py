# Generated by Django 5.1.1 on 2024-10-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseEnroll', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='points_assigned',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
