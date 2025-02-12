# Generated by Django 5.1.3 on 2025-02-06 17:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата и время последнего обновления', verbose_name='Дата обновления')),
                ('name', models.CharField(help_text='Введите название категории', max_length=255, unique=True, verbose_name='Название категории')),
                ('icon', models.ImageField(blank=True, help_text='Загрузите изображение для категории (необязательно)', null=True, upload_to='categories/', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата и время последнего обновления', verbose_name='Дата обновления')),
                ('title', models.CharField(help_text='Введите название объявления', max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(help_text='Введите описание объявления', verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, help_text='Введите стоимость объявления', max_digits=10, verbose_name='Цена')),
                ('currency', models.CharField(choices=[('USD', '$'), ('KGS', 'сом')], default='USD', help_text='Выберите валюту (USD или KGS)', max_length=3, verbose_name='Валюта')),
                ('location', models.CharField(help_text='Укажите местоположение объявления', max_length=255, verbose_name='Местоположение')),
                ('image', models.ImageField(blank=True, help_text='Загрузите изображение объявления (необязательно)', null=True, upload_to='products/', verbose_name='Фото')),
                ('category', models.ForeignKey(help_text='Выберите категорию для объявления', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Product.category', verbose_name='Категория')),
                ('owner', models.ForeignKey(help_text='Пользователь, разместивший объявление', on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время добавления в избранное', verbose_name='Дата добавления')),
                ('user', models.ForeignKey(help_text='Пользователь, добавивший продукт в избранное', on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('product', models.ForeignKey(help_text='Продукт, добавленный в избранное', on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='Product.product', verbose_name='Объявление')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранные',
                'ordering': ['-added_at'],
                'unique_together': {('user', 'product')},
            },
        ),
    ]
