# Generated by Django 3.2.8 on 2021-10-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('supermarket', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Product',
                'db_table': 'product',
            },
        ),
    ]