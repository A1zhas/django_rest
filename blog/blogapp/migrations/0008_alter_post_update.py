# Generated by Django 3.2.25 on 2025-02-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='update',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
