# Generated by Django 5.0.4 on 2024-05-04 04:37

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=100, verbose_name='Familiya')),
                ('username', models.CharField(blank=True, max_length=100, verbose_name='Username')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='E-mail manzil')),
                ('profile_image', models.ImageField(blank=True, default='images/profile_image.png', null=True, upload_to='images/', verbose_name='Profil rasmi')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Xodimlik statusi')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser statusi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Akkauntning faollik statusi')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('hobbies', models.ManyToManyField(to='app_users.hobby')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_users.student')),
            ],
        ),
    ]
