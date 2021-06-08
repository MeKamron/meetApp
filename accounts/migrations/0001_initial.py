# Generated by Django 3.2.4 on 2021-06-08 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Viloyat nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('keyword', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/photos/')),
                ('manzil', models.CharField(blank=True, max_length=300)),
                ('bio', models.CharField(max_length=512)),
                ('category', models.ManyToManyField(related_name='users', to='blog.Category')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.region')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.status')),
                ('sub_category', models.ManyToManyField(related_name='users', to='blog.SubCategory')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]