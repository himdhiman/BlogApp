# Generated by Django 3.0.6 on 2021-01-08 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201221_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main.comment'),
            preserve_default=False,
        ),
    ]
