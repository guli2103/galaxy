# Generated by Django 4.1.3 on 2022-12-14 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_rang_alter_mainpost_content_alter_mainpost_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moshin1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255)),
                ('rangi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.rang')),
            ],
        ),
    ]
