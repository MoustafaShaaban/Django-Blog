# Generated by Django 4.2.3 on 2024-01-30 03:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_alter_post_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="email",
        ),
    ]
