# Generated by Django 3.2 on 2021-05-05 18:48

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0015_alter_recipemodel_mealtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='mealtype',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Śniadanie', 'Śniadanie'), ('Drugie śniadanie', 'Drugie śniadanie'), ('Lunch do pracy', 'Lunch do pracy'), ('Obiad', 'Obiad'), ('Kolacja', 'Kolacja')], max_length=500, null=True),
        ),
    ]