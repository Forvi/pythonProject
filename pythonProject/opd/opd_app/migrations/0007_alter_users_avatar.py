# Generated by Django 5.0.4 on 2024-05-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd_app', '0006_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(upload_to='images/avatar/'),
        ),
    ]
