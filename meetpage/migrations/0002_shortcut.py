# Generated by Django 2.2.3 on 2019-07-31 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortCut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortcut', models.CharField(max_length=50, unique=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetpage.Appointment')),
            ],
        ),
    ]
