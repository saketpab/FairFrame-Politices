# Generated by Django 5.1.4 on 2025-01-02 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_remove_article_title_article_a_title_article_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='a_title',
            new_name='article_title',
        ),
    ]
