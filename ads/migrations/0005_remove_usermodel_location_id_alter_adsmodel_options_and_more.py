# Generated by Django 4.0.5 on 2022-07-05 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('ads', '0004_remove_adsmodel_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='location_id',
        ),
        migrations.AlterModelOptions(
            name='adsmodel',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='categoriesmodel',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='adsmodel',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.usermodel'),
        ),
        migrations.AlterField(
            model_name='adsmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='LocationModel',
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
