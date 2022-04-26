# Generated by Django 4.0.2 on 2022-04-18 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_user_delete_postperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=15)),
                ('patronymic', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('telnumber', models.IntegerField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Регистрация',
                'verbose_name_plural': 'Регистрация',
                'ordering': ['name', 'lastname'],
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]