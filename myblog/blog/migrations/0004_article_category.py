# Generated by Django 2.2.10 on 2020-03-03 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200302_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default=0, max_length=30, verbose_name='文章分类'),
        ),
    ]
