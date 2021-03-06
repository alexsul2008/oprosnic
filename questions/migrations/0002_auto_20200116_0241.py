# Generated by Django 3.0.2 on 2020-01-15 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='doc_url',
            field=models.CharField(max_length=250, verbose_name='Ссылка на документ'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='image',
            field=models.ImageField(null=True, upload_to='guestions/', verbose_name='Изображение'),
        ),
    ]
