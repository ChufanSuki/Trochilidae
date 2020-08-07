# Generated by Django 3.0.3 on 2020-08-07 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', help_text='avatar', upload_to='profile_pics')),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (0, 'Female'), (-1, 'Sercet')])),
                ('lastIp', models.GenericIPAddressField(verbose_name='Last Login IP')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nickname', models.CharField(blank=True, max_length=50)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('birthday', models.DateTimeField(blank=True)),
                ('company', models.CharField(blank=True, help_text='Your company name.e.g. Google', max_length=50)),
                ('role', models.CharField(blank=True, max_length=50)),
                ('rankId', models.IntegerField(default=0)),
                ('money', models.FloatField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('question', models.CharField(blank=True, help_text='Security Question.e.g. Where were I born?', max_length=50, verbose_name='Security Question')),
                ('answer', models.CharField(blank=True, help_text='Answer to Security Question.', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaintainerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', help_text='avatar', upload_to='profile_pics')),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (0, 'Female'), (-1, 'Sercet')])),
                ('lastIp', models.GenericIPAddressField(verbose_name='Last Login IP')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Real Name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
