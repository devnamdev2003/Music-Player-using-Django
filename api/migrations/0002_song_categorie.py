# Generated by Django 4.2.6 on 2024-01-29 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='categorie',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]