from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты
}

<<<<<<< HEAD
def recipe_get(request):
    re
=======

def get_recipes(request, dish, data=DATA):
    servings = request.GET.get('servings', 1)
    ingredients = {k: v * int(servings) for k, v in data.get(dish).items()}
    context = {
        'recipe': ingredients
    }
    return render(request, 'calculator/index.html', context)
>>>>>>> 8daa7f83db01fb759277fb5edb5cb2f6b2d0a7c8

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
