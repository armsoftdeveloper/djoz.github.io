# Generated by Django 4.2.3 on 2023-08-02 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_blogdetailview_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetailview',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
