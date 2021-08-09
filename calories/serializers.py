from rest_framework import serializers

import cooking
from cooking.models import IngredientsModel


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = cooking.models.IngredientsModel
        fields = (
            'name',
            'energy',
            'fat',
            'carbohydrates',
            'fiber',
            'protein',
            'salt',
            'sugar',
                  )

