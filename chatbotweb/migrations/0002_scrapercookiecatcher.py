# Generated by Django 3.1.6 on 2021-03-26 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScraperCookieCatcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookies_data', models.JSONField()),
                ('catching_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
