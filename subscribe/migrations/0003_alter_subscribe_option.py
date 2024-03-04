# Generated by Django 4.2.4 on 2024-01-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_subscribe_option_alter_subscribe_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly')], default='M', max_length=2),
        ),
    ]