# Generated by Django 4.1.1 on 2022-09-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diya', '0020_aboutus_con_head_aboutus_con_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='banner_img',
            field=models.ImageField(default='exit', upload_to='thumnail/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='banner_img1',
            field=models.ImageField(default='exit', upload_to='thumnail/'),
            preserve_default=False,
        ),
    ]