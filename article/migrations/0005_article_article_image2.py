# Generated by Django 4.1.1 on 2022-09-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_options_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Image 2'),
        ),
    ]
