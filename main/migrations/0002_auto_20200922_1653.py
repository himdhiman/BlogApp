# Generated by Django 3.0.8 on 2020-09-22 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='creadtedAt',
            new_name='createdAt',
        ),
    ]
