# Generated by Django 4.2.3 on 2023-08-02 11:31

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_blogdetail_quote_blogdetail_quote_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='quote',
            field=models.TextField(blank=True, help_text='Its Not Important To Write Quote', null=True, verbose_name='Set Quote'),
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='quote_author',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Quote Author'),
        ),
    ]
