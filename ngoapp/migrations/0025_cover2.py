# Generated by Django 3.2 on 2021-09-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngoapp', '0024_volunteerimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='cover2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=800)),
                ('image', models.ImageField(upload_to='cover2/')),
            ],
        ),
    ]
