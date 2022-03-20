# Generated by Django 4.0.3 on 2022-03-19 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('state', models.CharField(blank=True, max_length=255)),
                ('country_code', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('feels_like', models.FloatField()),
                ('datetime', models.DateTimeField()),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.city')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Погода',
                'verbose_name_plural': 'Погода',
                'db_table': 'weather',
            },
        ),
    ]
