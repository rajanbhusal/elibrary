# Generated by Django 5.0.1 on 2024-02-01 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookID', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('publishedDate', models.DateField()),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('membershipDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('detailsID', models.UUIDField(primary_key=True, serialize=False)),
                ('numberOfPages', models.PositiveIntegerField()),
                ('publisher', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=50)),
                ('bookID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.book')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowedBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowedDate', models.DateField()),
                ('returnDate', models.DateField(blank=True, null=True)),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.book')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.user'),
        ),
    ]
