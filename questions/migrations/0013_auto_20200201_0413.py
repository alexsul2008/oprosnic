# Generated by Django 3.0.2 on 2020-02-01 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_auto_20200201_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersanswers',
            name='not_ok_vop',
            field=models.IntegerField(default=0, null=True, verbose_name='Не правильный ответ'),
        ),
        migrations.AlterField(
            model_name='usersanswers',
            name='ok_vop',
            field=models.IntegerField(default=0, null=True, verbose_name='Правильный ответ'),
        ),
    ]
