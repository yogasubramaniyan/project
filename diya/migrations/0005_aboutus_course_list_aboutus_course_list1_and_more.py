# Generated by Django 4.1.1 on 2022-09-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diya', '0004_aboutus_course_head_aboutus_course_para'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='course_list',
            field=models.ImageField(default='exit', upload_to='thumnail/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='course_list1',
            field=models.ImageField(default='exit', upload_to='thumnail/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='course_list2',
            field=models.ImageField(default='exit', upload_to='thumnail/'),
            preserve_default=False,
        ),
    ]
