# Generated by Django 5.1.3 on 2024-11-30 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0010_rename_author_book_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='library_management.author'),
        ),
    ]
