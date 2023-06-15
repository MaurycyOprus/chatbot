import json


def get_by_type(type_val):

    with open('database.json') as file:
        data = json.load(file)

    list_of_type = []
    # get all values of a type
    for key in data["database"]:
        value = data["database"][key]
        for val in value:
            if val.get("type") == type_val:
                list_of_type.append(val.get("name"))

    return list_of_type


def if_in_database(name):

    with open('database.json') as file:
        data = json.load(file)

    for key in data["database"]:
        value = data["database"][key]
        for val in value:
            if val.get("name") == name:
                return True

    return False
            

def get_by_name(name):

    with open('database.json') as file:
        data = json.load(file)

    for key in data["database"]:
        value = data["database"][key]
        for val in value:
            if str(val.get("name")) == name:
                return val

    return None

