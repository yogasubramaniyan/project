# Generated by Django 4.1.1 on 2022-09-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diya', '0014_aboutus_rank_para2_aboutus_rank_para3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='Uk_para',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='Uk_para1',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='Uk_para2',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='Uk_para3',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='Uk_para4',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='Uk_para5',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
