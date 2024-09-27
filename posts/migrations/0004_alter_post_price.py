# Generated by Django 4.2 on 2024-09-27 20:29

from decimal import Decimal
import django.core.validators
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_contact_email_alter_post_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.00'), default_currency='GBP', max_digits=14, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
