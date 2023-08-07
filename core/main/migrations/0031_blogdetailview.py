# Generated by Django 4.2.3 on 2023-08-01 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_blog_delete_blogdetailview'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetailView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Set Title')),
                ('sub_title', models.CharField(max_length=50, verbose_name='Set Sub Title')),
                ('description', models.TextField(verbose_name='Set Description')),
                ('set_date', models.DateField(verbose_name='Set Date')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published ?')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.blog', verbose_name='Select Type')),
            ],
            options={
                'verbose_name': 'Blog Detail View',
                'verbose_name_plural': 'Blog Detail Views',
            },
        ),
    ]