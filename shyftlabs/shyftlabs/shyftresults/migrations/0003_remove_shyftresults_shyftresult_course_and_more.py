# Generated by Django 4.2.1 on 2023-05-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shyftresults', '0002_shyftresults_isdeleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shyftresults',
            name='shyftresult_course',
        ),
        migrations.RemoveField(
            model_name='shyftresults',
            name='shyftresult_user',
        ),
        migrations.AddField(
            model_name='shyftresults',
            name='shyft_coursename',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shyftresults',
            name='shyft_username',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
