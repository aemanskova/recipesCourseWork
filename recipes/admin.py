# from django.contrib import admin

# from recipes.models import Recipe, Ingredient, IngredientAmount, Tag


# class IngredientAmountInline(admin.TabularInline):
#     model = IngredientAmount
#     extra = 1


# @admin.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'name',
#         'author',
#         'cooking_time',
#     )
#     list_display_links = (
#         'id',
#         'name',
#         'author',
#     )

#     list_filter = (
#         'author__username',
#         'cooking_time',
#         'tags__name',
#     )
#     search_fields = (
#         'name',
#         'author__username',
#         'cooking_time',
#         'tags__name',
#     )
#     filter_horizontal = ("tags",)
#     inlines = (IngredientAmountInline,)
#     date_hierarchy = 'pub_date'
#     raw_id_fields = ('author',)


# @admin.register(Ingredient)
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'name',
#         'measurement_unit',
#     )
#     list_display_links = (
#         'id',
#         'name',
#         'measurement_unit',
#     )

#     list_filter = (
#         'name',
#         'measurement_unit',
#     )
#     search_fields = (
#         'name',
#         'measurement_unit',
#     )


# @admin.register(IngredientAmount)
# class IngredientAmountAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'ingredient',
#         'recipe',
#         'amount',
#     )
#     list_display_links = (
#         'id',
#         'ingredient',
#         'recipe',
#         'amount',
#     )

#     list_filter = (
#         'ingredient__name',
#         'recipe__name',
#     )
#     search_fields = (
#         'ingredient__name',
#         'recipe__name',
#     )


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'name',
#         'color',
#     )
#     list_display_links = (
#         'id',
#         'name',
#         'color'
#     )

#     list_filter = (
#         'name',
#         'color'
#     )
#     search_fields = (
#         'name',
#         'color',
#     )


from django.contrib import admin

from recipes.models import Recipe, Ingredient, IngredientAmount, Tag


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount
    extra = 1
    raw_id_fields = ('ingredient',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'cooking_time',
    )
    list_display_links = (
        'id',
        'name',
        'author',
    )

    list_filter = (
        'author__username',
        'cooking_time',
        'tags__name',
    )
    search_fields = (
        'name',
        'author__username',
        'cooking_time',
        'tags__name',
    )
    filter_horizontal = ("tags",)
    inlines = (IngredientAmountInline,)
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit',
    )
    list_display_links = (
        'id',
        'name',
        'measurement_unit',
    )

    list_filter = (
        'name',
        'measurement_unit',
    )
    search_fields = (
        'name',
        'measurement_unit',
    )


@admin.register(IngredientAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ingredient',
        'recipe',
        'amount',
    )
    list_display_links = (
        'id',
        'ingredient',
        'recipe',
        'amount',
    )

    list_filter = (
        'ingredient__name',
        'recipe__name',
    )
    search_fields = (
        'ingredient__name',
        'recipe__name',
    )
    raw_id_fields = ('ingredient',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
    )
    list_display_links = (
        'id',
        'name',
        'color'
    )

    list_filter = (
        'name',
        'color'
    )
    search_fields = (
        'name',
        'color',
    )