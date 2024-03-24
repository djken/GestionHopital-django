# Generated by Django 5.0.3 on 2024-03-24 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hopitaltracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom')),
                ('communaute', models.CharField(max_length=50, verbose_name='Communauté')),
                ('adresse', models.CharField(max_length=150, verbose_name='Adresse')),
                ('telephone', models.CharField(max_length=20, verbose_name='Telephone')),
                ('site', models.URLField(blank=True, max_length=150, null=True, verbose_name='Site')),
                ('courriel', models.EmailField(max_length=150, verbose_name='Courriel')),
            ],
            options={
                'db_table': 'hopitaltracker',
                'managed': True,
            },
        ),
    ]
