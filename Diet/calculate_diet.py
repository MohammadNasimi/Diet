from food.models import food
from exercise.models import exercise
def calculate(diet_data):
    print(diet_data)
    calories_give_all = 0
    for i in diet_data['food_Diet']:
        food_get = food.objects.get(id=i['food_field'])
        calories_give_all = calories_give_all + (food_get.calories*i['mesure_food_customer'])/food_get.mesure
    calories_lose_all = 0
    for j in diet_data['exercise_Diet']:
        exercise_get = exercise.objects.get(id=j['exersise_field'])
        calories_lose_all = calories_lose_all + (exercise_get.calories*j['time_exercise_customer'])/exercise_get.time

    calculate_calories = calories_give_all  - calories_lose_all
    return calculate_calories