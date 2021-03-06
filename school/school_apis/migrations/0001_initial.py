# Generated by Django 3.1.1 on 2020-10-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers_rooms', models.CharField(max_length=300)),
                ('numbers_students', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['numbers_rooms'],
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
