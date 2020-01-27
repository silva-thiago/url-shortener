# Generated by Django 2.2.9 on 2020-01-25 00:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generatedDate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('urlInput', models.CharField(blank=True, max_length=250, null=True)),
                ('urlOutput', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
