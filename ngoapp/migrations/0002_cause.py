# Generated by Django 3.2 on 2021-09-06 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=800)),
                ('image', models.ImageField(upload_to='cause/')),
            ],
        ),
    ]