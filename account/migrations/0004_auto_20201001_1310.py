# Generated by Django 3.1.1 on 2020-10-01 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190117_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='email_address',
            field=models.EmailField(max_length=100),
        ),
    ]