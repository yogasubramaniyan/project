# Generated by Django 4.1.1 on 2022-09-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diya', '0022_aboutus_logo_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='foot_logo',
            field=models.ImageField(default='exit', upload_to='thumnail/'),
            preserve_default=False,
        ),
    ]