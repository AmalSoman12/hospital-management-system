# Generated by Django 5.1.6 on 2025-02-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_alter_appoinment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='photo',
            field=models.ImageField(default=1, upload_to='doc_images'),
            preserve_default=False,
        ),
    ]
