# Generated by Django 4.0.5 on 2022-06-09 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('latitude', models.FloatField(max_length=32)),
                ('longitude', models.FloatField(max_length=32)),
                ('pricing', models.CharField(choices=[('$', 'Cheap'), ('$$', 'Moderate'), ('$$$', 'Expensive'), ('$$$$', 'Very Expensive')], max_length=4)),
                ('categories', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('lastLogin', models.DateField()),
                ('numSearches', models.IntegerField(max_length=16)),
                ('likedRestaurants', models.ManyToManyField(to='app.restaurant', verbose_name='list of liked restaurants')),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingThreshold', models.FloatField()),
                ('pricingRange', models.CharField(choices=[('$', 'Cheap'), ('$$', 'Moderate'), ('$$$', 'Expensive'), ('$$$$', 'Very Expensive')], max_length=4)),
                ('cuisineKeyword', models.CharField(max_length=60)),
                ('distance', models.IntegerField(max_length=3)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user', verbose_name='related user')),
            ],
        ),
    ]