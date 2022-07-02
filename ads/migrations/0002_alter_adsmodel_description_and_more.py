# Generated by Django 4.0.5 on 2022-07-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsmodel',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='adsmodel',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
