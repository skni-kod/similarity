from flask import flash

def sign_up_valid(email, first_name, password1, password2):
    if len(email) < 4:
        flash('Email must be longer than 3 characters', category='error')
        return False
    elif len(first_name) < 2:
        flash('Name must be longer than 1 character', category='error')
        return False
    elif password1 != password2:
        flash('Passwords doesn\'t match!', category='error')
        return False
    elif len(password1) < 7:
        flash('Password must be at least 7 characters', category='error')
        return False
    else:
        flash('Account created!', category='success')
        return True


def you_valid(gender, age, height, weight, silhouette, hair_colour, skin_colour, eye_colour):
    result = True
    # niepoprawnie sprawdza warunki. dla sylwetki sprawdza poprawnie, dla hair_colour, skin_colour... jakby ignorował, do naprawienia
    print(gender, age, height, weight, silhouette, hair_colour, skin_colour, eye_colour)
    if gender == '-':
        flash('You forgot to choose gender!', category='error')
        result = False

    if age == '':
        flash('You forgot to bring your age!', category='error')
        result = False

    elif int(age) < 0 or int(age) > 120:
        flash('Are you sure you\'re that old?', category='error')
        result = False

    if height == '':
        flash('You forgot to bring your height!', category='error')
        result = False

    elif int(height) < 50 or int(height) > 273:
        flash('Height is invalid!', category='error')
        result = False

    if weight == '':
        flash('You forgot to bring your weight!', category='error')
        result = False

    elif int(weight) < 10 or int(weight) > 610:
        flash('Weight is invalid!', category='error')
        result = False

    if hair_colour == '-':
        flash('You forgot to bring hair colour!', category='error')
        result = False

    if skin_colour == '-':
        flash('You forgot to bring skin colour!', category='error')
        result = False

    if eye_colour == '-':
        flash('You forgot to bring eye colour!', category='error')
        result = False

    if silhouette == '-':
        flash('You forgot to bring the silhouette!', category='error')
        result = False

    return result