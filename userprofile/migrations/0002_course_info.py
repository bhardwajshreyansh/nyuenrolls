# Generated by Django 5.1.1 on 2024-10-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_info',
            fields=[
                ('course_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('Instructor', models.CharField()),
                ('course_Capacity', models.IntegerField(max_length=3)),
                ('phd_course_capacity', models.IntegerField(max_length=3)),
                ('ta', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')])),
                ('class_day', models.DateField()),
                ('class_time', models.TimeField()),
                ('desciption', models.CharField(max_length=1000)),
                ('credits', models.DecimalField(decimal_places=1, max_digits=3)),
                ('students', models.ManyToManyField(to='userprofile.user_info')),
            ],
        ),
    ]