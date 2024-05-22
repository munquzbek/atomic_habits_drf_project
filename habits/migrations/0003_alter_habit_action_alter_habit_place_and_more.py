# Generated by Django 5.0.6 on 2024-05-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='action',
            field=models.CharField(max_length=300, verbose_name='action'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='place',
            field=models.CharField(max_length=50, verbose_name='place of action'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.DateTimeField(verbose_name='time of action'),
        ),
    ]
