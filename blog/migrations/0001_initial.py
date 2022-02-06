# Generated by Django 4.0.1 on 2022-01-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.ImageField(null=True, upload_to='', verbose_name='Head Image')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('main_text', models.TextField(null=True, verbose_name='Post content')),
                ('pub_date', models.DateTimeField(verbose_name='Publication date')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]
