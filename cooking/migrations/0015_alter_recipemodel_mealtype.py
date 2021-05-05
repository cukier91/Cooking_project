# Generated by Django 3.2 on 2021-05-05 18:47

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0014_alter_recipemodel_mealtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='mealtype',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Śniadanie'), (2, 'Drugie śniadanie'), (3, 'Lunch do pracy'), (4, 'Obiad'), (5, 'Kolacja')], max_length=500, null=True),
        ),
    ]
