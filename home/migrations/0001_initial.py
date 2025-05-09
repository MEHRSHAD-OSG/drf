# Generated by Django 5.1.7 on 2025-03-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
                ('age', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
