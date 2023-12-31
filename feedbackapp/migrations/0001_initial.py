# Generated by Django 3.2.13 on 2023-07-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('regNum', models.CharField(max_length=20)),
                ('mobile', models.PositiveIntegerField()),
                ('reason_for_visiting', models.TextField()),
                ('whom_did_you_meet', models.TextField()),
                ('description', models.TextField()),
                ('isProblemSolved', models.BooleanField()),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
    ]
