# Generated by Django 5.1.3 on 2024-12-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
