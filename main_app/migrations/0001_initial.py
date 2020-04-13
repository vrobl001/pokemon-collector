# Generated by Django 3.0.4 on 2020-04-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pokemon_type', models.CharField(max_length=100)),
                ('weakness', models.CharField(max_length=50)),
                ('lvl', models.IntegerField()),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]
