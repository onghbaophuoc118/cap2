# Generated by Django 3.0.10 on 2020-11-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_patient', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
                ('national', models.CharField(max_length=200)),
            ],
        ),
    ]
