# Generated by Django 5.0.6 on 2024-07-02 09:05

import bookings.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('overview', models.CharField(max_length=64)),
                ('highlight', models.CharField(max_length=64)),
                ('room_types', models.CharField(max_length=64)),
                ('rating', models.CharField(max_length=64)),
                ('price', models.FloatField(default=bookings.models.random_price)),
                ('imgurls', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='bookings_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='bookings_user_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='bookings.user')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_id', models.CharField(default='000', max_length=64)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=15)),
                ('room', models.IntegerField(default=1)),
                ('adult', models.IntegerField(default=1)),
                ('child', models.IntegerField(default=0)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(default=None)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='bookings.hotel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='bookings.user')),
            ],
        ),
    ]