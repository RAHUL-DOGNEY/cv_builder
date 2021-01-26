# Generated by Django 3.1.2 on 2021-01-17 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=1000)),
                ('skill', models.CharField(max_length=1000)),
                ('about_you', models.CharField(max_length=100)),
                ('previous_work', models.CharField(max_length=100)),
            ],
        ),
    ]
