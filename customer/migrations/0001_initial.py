# Generated by Django 2.0.1 on 2018-05-14 02:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('purchase', models.TextField()),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('deletedAt', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]