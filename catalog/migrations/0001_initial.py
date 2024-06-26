# Generated by Django 4.2.7 on 2024-05-03 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Назва')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'категорію',
                'verbose_name_plural': 'Категорії',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Назва товару')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('composition', models.TextField(blank=True, null=True, verbose_name='Склад товару)')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кільікість')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Ціна без знижки')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Знижка %')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Фотографія')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.categories', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товари',
                'db_table': 'product',
                'ordering': ('id',),
            },
        ),
    ]
