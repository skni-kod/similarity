# contains other functions
from .models import User

def number_of_similars(gender, age, height, weight, skin_colour):
    age = int(age)
    height = int(height)
    weight = int(weight)

    users = User.query.all()
    counter = int(0)
    for user in users:
        if (gender == gender and difference(age, user.age, 2) and difference(height, user.height, 3) and
                difference(weight, user.weight, 2) and skin_colour == user.skin_colour):
            counter += 1

    return counter


def number_of_identical(gender, age, height, weight, silhouette, hair_colour, facial_hair, glasses, skin_colour, eye_colour):

    age = int(age)
    height = int(height)
    weight = int(weight)

    number_of_identic = User.query.filter_by(
                                gender=gender, age=age, height=height, weight=weight, silhouette=silhouette,
                                hair_colour=hair_colour, facial_hair=facial_hair, glasses=glasses,
                                skin_colour=skin_colour, eye_colour=eye_colour
                                ).count()

    return number_of_identic


def difference(a, b, max_difference):
    a = int(a)
    max_difference = int(max_difference)

    if abs(a-b) <= max_difference:
        return True

    return False


def print_whole_table():
    users = User.query.all()
    for user in users:
        print(user.id, user.ipaddress, user.date ,user.gender, user.age, user.height, user.weight, user.silhouette, user.hair_colour, user.facial_hair, user.glasses, user.skin_colour, user.eye_colour)


def stat(column, argument):
    users = User.query.all()
    argument_counter = int(0)
    other_counter = int(0)

    for user in users:
        if (column==argument):
            argument_counter += 1
        else:
            other_counter +=1

    return argument_counter / (argument_counter+other_counter)