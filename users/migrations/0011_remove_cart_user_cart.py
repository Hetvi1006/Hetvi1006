# Generated by Django 2.2.3 on 2019-09-26 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190926_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user_cart',
        ),
    ]
