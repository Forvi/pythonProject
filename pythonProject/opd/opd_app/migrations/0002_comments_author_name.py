# Generated by Django 5.0.4 on 2024-05-14 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author_name',
            field=models.CharField(default=2, max_length=5),
            preserve_default=False,
        ),
    ]
