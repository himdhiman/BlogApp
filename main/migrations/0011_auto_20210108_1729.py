# Generated by Django 3.0.6 on 2021-01-08 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210108_1714'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comments']},
        ),
    ]