# Generated by Django 3.2 on 2021-09-06 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngoapp', '0010_auto_20210906_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourcaus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_description', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=800)),
                ('image', models.ImageField(upload_to='ourcause/')),
            ],
        ),
        migrations.DeleteModel(
            name='ourcause',
        ),
    ]