# Generated by Django 4.1.6 on 2023-02-15 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=63, validators=[django.core.validators.RegexValidator(message='Standard e-mail form', regex='^[a-zA-Z0-9]{1}[a-zA-Z0-9_]+(-{1})?[a-zA-Z0-9_]+@{1}([a-zA-Z0-9]+\\.)+[a-z0-9]{1}([a-z0-9-]*[a-z0-9])?$')])),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField(blank=True, max_length=1000)),
                ('date_of_the_request', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Contact Requests',
                'verbose_name_plural': 'Contact Requests',
                'ordering': ('-date_of_the_request',),
            },
        ),
    ]