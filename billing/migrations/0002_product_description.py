# Generated by Django 5.0.4 on 2024-05-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='default description'),
            preserve_default=False,
        ),
    ]
