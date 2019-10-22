# Generated by Django 2.2.4 on 2019-10-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
                ('expertise', models.CharField(max_length=10)),
                ('min_years_experience', models.IntegerField()),
            ],
        ),
    ]
