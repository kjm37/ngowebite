# Generated by Django 3.2 on 2021-09-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngoapp', '0026_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='causecover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=800)),
                ('image', models.ImageField(upload_to='ccover/')),
            ],
        ),
        migrations.CreateModel(
            name='contactuscover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=800)),
                ('image', models.ImageField(upload_to='concover/')),
            ],
        ),
        migrations.CreateModel(
            name='donatecover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=800)),
                ('image', models.ImageField(upload_to='dcover/')),
            ],
        ),
        migrations.CreateModel(
            name='donateteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=800)),
                ('image', models.ImageField(upload_to='donateteam/')),
            ],
        ),
        migrations.CreateModel(
            name='eventcover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=800)),
                ('image', models.ImageField(upload_to='ecover/')),
            ],
        ),
        migrations.CreateModel(
            name='gallerycover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=800)),
                ('image', models.ImageField(upload_to='gcover/')),
            ],
        ),
        migrations.RenameModel(
            old_name='cover2',
            new_name='aboutcover',
        ),
        migrations.RenameModel(
            old_name='cover',
            new_name='homecover',
        ),
    ]
