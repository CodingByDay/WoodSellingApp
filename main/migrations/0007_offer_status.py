# Generated by Django 3.1.1 on 2020-09-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200920_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
