# Generated by Django 3.1.3 on 2020-12-18 09:38

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
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tomhealth.category')),
            ],
        ),
    ]
