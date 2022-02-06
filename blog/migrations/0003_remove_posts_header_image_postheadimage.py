# Generated by Django 4.0.1 on 2022-01-23 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_posts_header_image_alter_posts_main_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='header_image',
        ),
        migrations.CreateModel(
            name='PostHeadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Header Image')),
                ('post', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.posts')),
            ],
        ),
    ]
