# Generated by Django 3.2 on 2021-09-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngoapp', '0008_datex'),
    ]

    operations = [
        migrations.CreateModel(
            name='datexx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('eventname', models.CharField(max_length=40)),
                ('cityname', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='datex',
        ),
    ]
