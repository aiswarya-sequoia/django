# Generated by Django 4.1.1 on 2022-09-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
