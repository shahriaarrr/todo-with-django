# Generated by Django 3.1.4 on 2021-08-21 06:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('Priority', models.CharField(choices=[('h', 'high'), ('l', 'low')], default='l', max_length=4)),
                ('task_text', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 8, 21, 6, 46, 1, 90495, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('task', django.db.models.manager.Manager()),
            ],
        ),
    ]
