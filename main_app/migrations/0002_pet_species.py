# Generated by Django 3.1.2 on 2020-10-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='species',
            field=models.CharField(default='cat', max_length=75),
            preserve_default=False,
        ),
    ]