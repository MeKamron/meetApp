# Generated by Django 3.2.4 on 2021-06-17 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_profile_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='manzil',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
