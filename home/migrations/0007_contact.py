# Generated by Django 3.2.13 on 2024-02-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20240212_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('description', models.TextField(blank=True)),
                ('icon', models.CharField(max_length=255)),
            ],
        ),
    ]