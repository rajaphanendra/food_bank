# Generated by Django 4.0.10 on 2023-12-07 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receiver', '0001_initial'),
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('meals_food_stock', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='meals.mealsfoodstock')),
                ('receiver', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='receiver.receiver')),
            ],
        ),
    ]
