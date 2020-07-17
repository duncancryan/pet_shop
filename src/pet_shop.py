# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] = pet_shop["admin"]["total_cash"] + cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] = pet_shop["admin"]["pets_sold"] + pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if breed == pet["breed"]:
            pets.append(pet)
    return pets

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet_name == pet["name"]:
            return pet
    return None

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet_name == pet["name"]:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# I want to create something that can define the inputs for all of the values in the new_pet dictionary
# At this point I'm not sure if that would pass the test
# but it seems like that would be better than trying to pass an entire dictionary into a funciton?
# test passing for now, going to come back to it at the end of the task, if it doesn't pass so be it, will comment it out.

def get_customer_cash(customer):
    return customer["cash"]

