# Generated by Django 4.2.4 on 2023-11-30 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='Article',
            field=models.CharField(max_length=30000),
        ),
    ]
