# Generated by Django 4.1.3 on 2022-11-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='click',
            new_name='explain',
        ),
        migrations.AddField(
            model_name='feed',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
