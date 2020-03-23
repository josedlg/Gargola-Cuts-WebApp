# Generated by Django 3.0.4 on 2020-03-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barberImage', models.ImageField(upload_to='barberPics', verbose_name='Barber Prof Pic')),
                ('barberBio', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('barberRules', models.CharField(blank=True, max_length=200, null=True, verbose_name='Rules')),
                ('styleImage', models.ImageField(upload_to='stylePics', verbose_name='New Style Picture')),
                ('adsImage', models.ImageField(upload_to='ads', verbose_name='Ads Flyer')),
            ],
        ),
    ]
