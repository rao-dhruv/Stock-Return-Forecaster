# Generated by Django 3.1.1 on 2021-04-16 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stockmarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Open', models.FloatField()),
                ('High', models.FloatField()),
                ('Low', models.FloatField()),
                ('Close', models.FloatField()),
            ],
        ),
    ]
