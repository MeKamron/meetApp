# Generated by Django 3.2.4 on 2021-06-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('accounts', '0004_auto_20210609_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sub_category',
            field=models.ManyToManyField(blank=True, related_name='users', to='blog.SubCategory'),
        ),
    ]
