# Generated by Django 2.1.7 on 2019-05-22 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circle',
            options={'get_latest_by': ['created'], 'ordering': ['-rides_taken', '-rides_offered']},
        ),
    ]
