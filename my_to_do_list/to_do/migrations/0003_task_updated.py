# Generated by Django 4.2.4 on 2023-08-11 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0002_alter_task_options_alter_task_order_with_respect_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]