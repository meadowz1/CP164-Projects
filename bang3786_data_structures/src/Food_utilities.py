"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-15"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    name = input("Name: ")
    
    for i, origin in enumerate(Food.ORIGIN):
        print(f"{i}. {origin}")
    origin_input = input("Enter the number corresponding to the origin: ")
    origin = int(origin_input)

    # Get vegetarian information from the user
    is_vegetarian_input = input("Vegetarian? (Y/N): ")
    is_vegetarian = is_vegetarian_input.lower() == 'Y'

    # Get calories information from the user
    calories_input = input("Calories: ")
    calories = int(calories_input) if calories_input.lower() != 'none' else None

    # Create and return the Food object
    food = Food(name, origin, is_vegetarian, calories)
    
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    parts = line.strip().split('|')
    
    name = parts[0]
    origin = int(parts[1])
    is_vegetarian = parts[2].lower() == 'true'
    calories = int(parts[3]) if parts[3].lower() != 'none' else None

    food = Food(name, origin, is_vegetarian, calories)
    
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """

    foods = []

    for line in file_variable:
        food = read_food(line.strip())
        foods.append(food)

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    for food in foods:
        file_variable.write(f"{food.name}|{food.origin}|{food.is_vegetarian}|{food.calories}\n")

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    veggies = [food for food in foods if food.is_vegetarian]

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    
    assert origin in range(len(Food.ORIGIN))
    
    origins = []

    for food in foods:
        
        if food.origin == origin:
            origins.append(food)

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    total_calories = 0

    if len(foods) == 0:
        total_calories

    else:
        for food in foods:
            total_calories += food.calories

        avg = total_calories / len(foods)

    avg = round(avg)
    
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    total_calories = 0
    count = 0

    for food in foods:
        if food.origin == origin:
            total_calories += food.calories
            count += 1

    if count > 0:
        avg = total_calories / count
    else:
        avg = 0
    
    avg = round(avg)
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    print("Food                         Origin          Vegetarian      Calories")
    print("-" * 75)

    for food in foods:
        veg_status = "True" if food.is_vegetarian else "False"

        food_name = (food.name + ' ' * 30)[:30]
        food_origin = (Food.ORIGIN[food.origin] + ' ' * 15)[:15]
        food_veg_status = (veg_status + ' ' * 15)[:15]
        food_calories = str(food.calories) + ' ' * 15

        food_calories = food_calories[:15]
        
        print(food_name + food_origin + food_veg_status + food_calories)

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []
    
    for food in foods:
        origin_matches = (origin == -1) or (food.origin == origin)

        cals_matches = (max_cals == 0) or (food.calories <= max_cals)

        veg_matches = (is_veg is False) or (food.is_vegetarian == is_veg)
     
        if origin_matches and cals_matches and veg_matches:
            result.append(food)

    return result





