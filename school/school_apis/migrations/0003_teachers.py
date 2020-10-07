# Generated by Django 3.1.1 on 2020-10-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_apis', '0002_auto_20201006_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names_of_teachers', models.CharField(max_length=100)),
                ('numbers_of_teachers', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['names_of_teachers'],
            },
        ),
    ]
