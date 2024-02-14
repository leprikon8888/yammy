# Generated by Django 3.2.13 on 2024-02-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery/')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('position',), 'verbose_name_plural': 'Events'},
        ),
    ]