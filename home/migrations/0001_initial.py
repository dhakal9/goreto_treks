# Generated by Django 5.0 on 2024-01-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=15)),
                ('slogan1', models.CharField(max_length=200)),
                ('slogan2', models.CharField(max_length=200)),
                ('about_heading', models.CharField(max_length=200)),
                ('about_thumbnail', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('about_us', models.TextField(max_length=2000)),
                ('home_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('banner1_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('banner2_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('logo_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('video_thumbnail_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('video_link', models.URLField(blank=True, db_index=True, max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExcludeInclude',
            fields=[
                ('funfact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Funfacts',
            fields=[
                ('funfact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('team_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('facebook_link', models.URLField(blank=True, db_index=True, max_length=128, unique=True)),
                ('instagram_link', models.URLField(blank=True, db_index=True, max_length=128, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
