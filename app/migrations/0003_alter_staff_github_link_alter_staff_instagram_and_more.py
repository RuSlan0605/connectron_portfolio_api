# Generated by Django 4.0 on 2023-05-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_staff_github_link_alter_staff_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='github_link',
            field=models.CharField(blank=True, default='https://github.com/', max_length=2048, null=True, unique=True, verbose_name='GitHub Link'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='instagram',
            field=models.CharField(blank=True, default='https://instagram.com/', max_length=2048, null=True, unique=True, verbose_name='Instagram Link'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='telegram',
            field=models.CharField(blank=True, default='https://t.me/', max_length=2048, null=True, unique=True, verbose_name='Telegram Link'),
        ),
    ]