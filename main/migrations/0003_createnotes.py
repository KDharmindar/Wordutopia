# Generated by Django 2.0.6 on 2018-07-10 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180710_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=250)),
                ('Content', models.CharField(default='', max_length=500)),
            ],
        ),
    ]