# Generated by Django 3.2.7 on 2021-09-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
