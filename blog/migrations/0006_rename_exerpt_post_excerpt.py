# Generated by Django 4.2.16 on 2024-11-14 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='exerpt',
            new_name='excerpt',
        ),
    ]
