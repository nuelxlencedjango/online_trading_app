# Generated by Django 4.1.12 on 2023-11-02 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_biz_current_balance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biz',
            options={'ordering': ['date_of_transaction']},
        ),
    ]
