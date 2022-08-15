from food.models import food,food_diet_admin,food_diet_user
from exercise.models import exercise,exercise_diet_admin,exercise_diet_user
from customer.models import customer
from Diet.models import Diet_admin
import random
def calculate(diet_data):
    #customer
    customer_diet = customer.objects.get(id=diet_data['user'])
    calories_give_all = 0
    food_diet_user_id =[]                            
    for i in diet_data['food_Diet']:
        food_get = food.objects.get(id=i['food_field'])
        calories_give_all = calories_give_all + (food_get.calories*i['mesure_food_customer'])/food_get.mesure
        food_diet_user_get=food_diet_user.objects.create(customer_food=customer_diet,food_field=food_get,
                                        mesure_food_customer=i['mesure_food_customer'])
        food_diet_user_id.append(food_diet_user_get.id)

    ############################################################
    exercise_diet_user_id =[]                            

    calories_lose_all = 0
    for j in diet_data['exercise_Diet']:
        exercise_get = exercise.objects.get(id=j['exersise_field'])
        calories_lose_all = calories_lose_all + (exercise_get.calories*j['time_exercise_customer'])/exercise_get.time
        exercise_diet_user_get=exercise_diet_user.objects.create(customer_exercise=customer_diet,exersise_field=exercise_get,
                                        time_exercise_customer=j['time_exercise_customer'])
        exercise_diet_user_id.append(exercise_diet_user_get.id)

    calculate_calories = calories_give_all  - calories_lose_all 

    ###################create Diets admin ##############
    # Diet_admin.objects.create(user_admin=customer_diet,food_Diet_admin = [])

    #food
    foods = food.objects.all()
    foods_count = foods.count()
    mesure_all_foods = 0
    food_diet_admin_id =[]
    for M in range(1,len(diet_data['food_Diet'])+1):
        food_id = random.randint(1,foods_count)
        food_admin = food.objects.get(id = food_id)
        user_admin = customer_diet
        mesure_food_admin = random.randint(5,50)
        ##################################
        mesure_all_foods = mesure_all_foods +(food_admin.calories*mesure_food_admin)/food_admin.mesure
        food_diet_admin_get =food_diet_admin.objects.create(admin_food=user_admin,food_field_admin=food_admin,
                                        mesure_food_admin=mesure_food_admin)

        food_diet_admin_id.append(food_diet_admin_get.id)



    #exercise
    exercises = exercise.objects.all()
    exercises_count = exercises.count()
    mesure_all_exercises = 0
    exercise_diet_admin_id = []
    for N in range(1,len(diet_data['exercise_Diet'])+1):
        exercise_id = random.randint(1,exercises_count)
        exersise_field_admin = exercise.objects.get(id = exercise_id)
        admin_exercise = customer_diet
        time_exercise_admin = random.randint(5,50)
        mesure_all_exercises = mesure_all_exercises +(exersise_field_admin.calories*time_exercise_admin)/exersise_field_admin.time

        exercise_diet_admin_get =exercise_diet_admin.objects.create(admin_exercise=admin_exercise,
                                exersise_field_admin=exersise_field_admin,time_exercise_admin=time_exercise_admin)
        
        exercise_diet_admin_id.append(exercise_diet_admin_get.id) 
        
    calculate_admin_calories = mesure_all_foods - mesure_all_exercises

    if calculate_admin_calories > 0 :
        exercise_id = random.randint(1,exercises_count)
        exersise_field_admin = exercise.objects.get(id = exercise_id)
        admin_exercise = customer_diet
        time_exercise_admin = (calculate_admin_calories*exersise_field_admin.time)/exersise_field_admin.calories
        mesure_all_exercises = mesure_all_exercises + calculate_admin_calories
        exercise_diet_admin_get =exercise_diet_admin.objects.create(admin_exercise=admin_exercise,
                                exersise_field_admin=exersise_field_admin,time_exercise_admin=time_exercise_admin)
        exercise_diet_admin_id.append(exercise_diet_admin_get.id)
    elif calculate_admin_calories< 0:
        food_id = random.randint(1,foods_count)
        food_admin = food.objects.get(id = food_id)
        user_admin = customer_diet
        mesure_food_admin = (abs(calculate_admin_calories)*food_admin.mesure)/food_admin.calories
        mesure_all_foods = mesure_all_foods + abs(calculate_admin_calories)
        ##################################
        food_diet_admin_get = food_diet_admin.objects.create(admin_food=user_admin,food_field_admin=food_admin,
                                        mesure_food_admin=mesure_food_admin)
        food_diet_admin_id.append(food_diet_admin_get.id)


    calculate_admin_calories = mesure_all_foods - mesure_all_exercises
    

    ##################################kind_diet#######################################
    if diet_data['kind_diet'] == "1" :
        exercise_id = random.randint(1,exercises_count)
        exersise_field_admin = exercise.objects.get(id = exercise_id)
        admin_exercise = customer_diet
        time_exercise_admin = random.randint(5,50)

        exercise_diet_admin_get =exercise_diet_admin.objects.create(admin_exercise=admin_exercise,
                                exersise_field_admin=exersise_field_admin,time_exercise_admin=time_exercise_admin)
        
        exercise_diet_admin_id.append(exercise_diet_admin_get.id) 
    elif diet_data['kind_diet'] == "3":
        food_id = random.randint(1,foods_count)
        food_admin = food.objects.get(id = food_id)
        user_admin = customer_diet
        mesure_food_admin = random.randint(5,50)
        ##################################
        mesure_all_foods = mesure_all_foods +(food_admin.calories*mesure_food_admin)/food_admin.mesure
        food_diet_admin_get =food_diet_admin.objects.create(admin_food=user_admin,food_field_admin=food_admin,
                                        mesure_food_admin=mesure_food_admin)

    return [customer_diet,food_diet_admin_id,exercise_diet_admin_id,food_diet_user_id,
            exercise_diet_user_id,diet_data['kind_diet']]