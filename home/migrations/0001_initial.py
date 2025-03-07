# Generated by Django 5.1.6 on 2025-03-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1500)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]
