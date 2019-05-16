# Generated by Django 2.0.2 on 2019-02-17 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('ip', models.GenericIPAddressField()),
                ('log_key', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='log_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.User'),
        ),
    ]