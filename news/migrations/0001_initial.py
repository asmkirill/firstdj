# Generated by Django 4.1.7 on 2023-03-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name of title')),
                ('announcement', models.CharField(max_length=250, verbose_name='Announcement')),
                ('full_text', models.TextField(verbose_name='Article')),
                ('date', models.DateTimeField(verbose_name='Date of publishing')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
