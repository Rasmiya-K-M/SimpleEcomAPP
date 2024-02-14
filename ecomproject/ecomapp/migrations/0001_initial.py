# Generated by Django 4.2.9 on 2024-02-04 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=250, unique=True)),
                ('cslug', models.SlugField(max_length=250, unique=True)),
                ('cdesc', models.TextField(blank=True)),
                ('cimage', models.ImageField(blank=True, upload_to='category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('cname',),
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=250, unique=True)),
                ('pslug', models.SlugField(max_length=250, unique=True)),
                ('pdesc', models.TextField(blank=True)),
                ('pprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pimage', models.ImageField(blank=True, upload_to='product')),
                ('pstock', models.IntegerField()),
                ('pavail', models.BooleanField(default=True)),
                ('pcreated', models.DateField(auto_now_add=True)),
                ('pupdated', models.DateField(auto_now_add=True)),
                ('pcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'productss',
                'ordering': ('pname',),
            },
        ),
    ]
