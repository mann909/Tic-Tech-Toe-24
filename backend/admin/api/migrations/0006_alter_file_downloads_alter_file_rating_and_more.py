# Generated by Django 5.1 on 2024-09-28 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_file_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='downloads',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='rating',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='views',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]