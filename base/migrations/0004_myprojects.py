# Generated by Django 5.2 on 2025-04-10 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_delete_myskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myprojects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pdesc', models.TextField()),
            ],
        ),
    ]
