# Generated by Django 2.1 on 2018-08-19 14:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_mod_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='category',
            name='last_mod_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='last_mod_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
    ]
