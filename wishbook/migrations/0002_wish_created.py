# Generated by Django 2.2 on 2019-04-19 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wishbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
