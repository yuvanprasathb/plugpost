# Generated by Django 4.2.4 on 2023-12-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_blogs_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='Blog_User',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]