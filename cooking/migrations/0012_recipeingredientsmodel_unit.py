# Generated by Django 3.2 on 2021-05-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0011_alter_recipemodel_mealtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredientsmodel',
            name='unit',
            field=models.CharField(choices=[('ML', 'ml'), ('L', 'l'), ('G', 'g'), ('KO', 'dag'), ('KG', 'kg'), ('Ł', 'łyżka'), ('ŁY', 'łyżki'), ('ł', 'łyżeczka'), ('ły', 'łyżeczki')], max_length=50, null=True),
        ),
    ]
