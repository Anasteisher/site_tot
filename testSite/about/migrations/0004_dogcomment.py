# Generated by Django 4.2.7 on 2023-12-14 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=40)),
                ('feedback', models.CharField(max_length=400)),
                ('checkbox', models.BooleanField(default=False)),
            ],
        ),
    ]