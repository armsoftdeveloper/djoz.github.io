# Generated by Django 4.2.3 on 2023-08-02 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_remove_blogdetailview_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogDetailView',
            new_name='BlogDetail',
        ),
    ]
