# Lasagna Cooking Details

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def remaining_min_in_oven(bake_time: int) -> int:
    """
    This function takes the amount of time in the oven and subtracts it from the average cook
    time of 40min to calculate time remaining
    """
    return EXPECTED_BAKE_TIME - bake_time

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    This function takes the total amount of layers added to the lasagna and multiplies
    the total by 2, which is the average prep time per a layer
    """
    return PREPARATION_TIME * number_of_layers

def total_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """
    This function takes total layers of lasagna and adds the time needed to cook
    it to calculate cook time and prep time together
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time


print (total_time_in_minutes(2,23))
