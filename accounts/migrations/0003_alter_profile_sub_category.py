# Generated by Django 3.2.4 on 2021-06-09 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('accounts', '0002_remove_status_keyword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sub_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='blog.SubCategory'),
        ),
    ]