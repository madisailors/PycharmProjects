# Generated by Django 4.1.3 on 2022-11-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityclasses',
            name='instructor_name',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
    ]
