# Generated by Django 4.0.2 on 2022-09-03 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docsapp', '0005_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.IntegerField(blank=True),
        ),
    ]
