# Generated by Django 5.1.6 on 2025-02-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoinment',
            name='status',
            field=models.CharField(choices=[('visited', 'Visited'), ('not visited', 'Not Visited')], default='not_visited', max_length=20),
        ),
    ]
