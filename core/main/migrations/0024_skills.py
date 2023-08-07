# Generated by Django 4.2.3 on 2023-07-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_delete_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Set Title')),
                ('sub_title', models.CharField(max_length=50, verbose_name='Set Subtitle')),
                ('img', models.ImageField(upload_to='media/%Y-%m-%d', verbose_name='Upload Image')),
                ('description', models.TextField(verbose_name='Set Description')),
                ('url', models.URLField(verbose_name='Set Video Url')),
                ('option_first_title', models.CharField(max_length=50, verbose_name='Option First Title')),
                ('option_first_range', models.CharField(max_length=50, verbose_name='Option First Range')),
                ('option_second_title', models.CharField(max_length=50, verbose_name='Option Second Title')),
                ('option_second_range', models.CharField(max_length=50, verbose_name='Option Second Range')),
                ('option_third_title', models.CharField(max_length=50, verbose_name='Option Third Title')),
                ('option_third_range', models.CharField(max_length=50, verbose_name='Option Third Range')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published ?')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
            ],
        ),
    ]
