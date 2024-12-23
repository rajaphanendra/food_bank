# Generated by Django 4.0.10 on 2023-12-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_donate_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='unit',
            field=models.CharField(choices=[('oz', 'Ounces'), ('lb', 'Pounds')], default='lb', max_length=2),
        ),
    ]