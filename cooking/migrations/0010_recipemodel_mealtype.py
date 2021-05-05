# Generated by Django 3.2 on 2021-05-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0009_alter_recipemodel_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipemodel',
            name='mealtype',
            field=models.CharField(choices=[('SN', 'Śniadanie'), ('DSN', 'Drugie śniadanie')], max_length=50, null=True),
        ),
    ]
