# Generated by Django 4.2.7 on 2023-12-02 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(null=True),
        ),
    ]
