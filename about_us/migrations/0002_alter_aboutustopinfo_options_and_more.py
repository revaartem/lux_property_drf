# Generated by Django 4.1.6 on 2023-02-15 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutustopinfo',
            options={'verbose_name': 'Top info block', 'verbose_name_plural': 'Top info blocks'},
        ),
        migrations.AlterModelOptions(
            name='firstbenefitsblock',
            options={'verbose_name': 'First benefits block', 'verbose_name_plural': 'First benefit blocks'},
        ),
        migrations.AlterModelOptions(
            name='photosandnumbers',
            options={'verbose_name': 'Photos and numbers block', 'verbose_name_plural': 'Photos and numbers blocks'},
        ),
        migrations.AlterModelOptions(
            name='secondbenefitsblock',
            options={'verbose_name': 'Second benefits block', 'verbose_name_plural': 'Second benefits blocks'},
        ),
        migrations.AlterModelOptions(
            name='teammember',
            options={'verbose_name': 'Team member', 'verbose_name_plural': 'Team members'},
        ),
    ]