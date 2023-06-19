from rest_framework import serializers
from django.contrib.auth import get_user_model

from recipes.models import Recipe

User = get_user_model()


class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "description",
            "cooking_time",
            "pub_date",
        )


class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "description",
            "author",
            "cooking_time",
            "pub_date",

        )
