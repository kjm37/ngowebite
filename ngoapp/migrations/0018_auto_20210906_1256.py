# Generated by Django 3.2 on 2021-09-06 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngoapp', '0017_auto_20210906_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tdata',
            old_name='title',
            new_name='head',
        ),
        migrations.RenameField(
            model_name='tdata2',
            old_name='title',
            new_name='head',
        ),
        migrations.RenameField(
            model_name='tdata2',
            old_name='description',
            new_name='text',
        ),
    ]
