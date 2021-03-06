# Generated by Django 3.0.2 on 2020-01-15 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Группа отдела')),
                ('can_drop', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Группа отдела',
                'verbose_name_plural': 'Группы отдела',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Вопрос')),
                ('in_active', models.BooleanField(default=True, verbose_name='Активность вопроса')),
                ('image', models.ImageField(upload_to='guestions/', verbose_name='Изображение')),
                ('doc_url', models.SlugField(verbose_name='Ссылка на документ')),
                ('groups', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questions.UserGroups', verbose_name='группа отдела')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Текст ответа')),
                ('approved', models.BooleanField(default=False, verbose_name='Правильность ответа')),
                ('vop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Questions', verbose_name='вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
