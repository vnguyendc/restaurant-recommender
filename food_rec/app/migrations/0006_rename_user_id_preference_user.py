# Generated by Django 4.0.5 on 2022-07-18 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preference',
            old_name='user_id',
            new_name='user',
        ),
    ]
