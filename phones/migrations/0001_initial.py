# Generated by Django 2.2.10 on 2020-08-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('name', models.TextField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('lte_exists', models.BooleanField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'phones',
            },
        ),
    ]
