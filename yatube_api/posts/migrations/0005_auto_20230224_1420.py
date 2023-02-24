# Generated by Django 3.2.16 on 2023-02-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_group'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='follow',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='user',
            new_name='follower',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('follower', 'following'), name='follow'),
        ),
    ]
