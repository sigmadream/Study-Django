# Generated by Django 3.1.5 on 2021-02-05 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Tag')),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'PUblished')], default='draft', max_length=10, verbose_name='Status')),
                ('publication_data', models.DateTimeField(verbose_name='Created')),
                ('picture', models.ImageField(upload_to='uploads/%Y/%m/%d', verbose_name='Picture')),
                ('content', models.TextField(verbose_name='Content')),
                ('author', models.CharField(default='Anonymous', max_length=30, verbose_name='Created by')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.category', verbose_name='Category')),
                ('tags', models.ManyToManyField(to='post.Tag')),
            ],
        ),
    ]
