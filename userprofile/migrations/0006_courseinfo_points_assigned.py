# Generated by Django 5.1.1 on 2024-10-19 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_admininfo_departmentinfo_alter_studentinfo_n_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinfo',
            name='points_assigned',
            field=models.CharField(max_length=3, null=True),
        ),
    ]