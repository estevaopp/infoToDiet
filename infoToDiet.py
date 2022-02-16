def main():
    height = getheight()
    weight = getweight()
    age = getage()
    gender = getgender()
    tmb = calcTMB(height, weight, age, gender)
    activety = boolactive()
    get = calcGET(tmb, activety)
    protein = calcProtein(weight)
    fat = calcFat(weight)
    print(f'Você tem que comer {get} cal por dia.')
    print(f'{protein}g proteina')
    print(f'{fat}g gordura')

def getheight():
    while True:
        try:
            height = input('Altura (em cm): ')
            height = float(height.replace(',', '.'))
            if height > 100:
                break
        except:
            print('Escreva a sua altura em cm.')
    return height

def getweight():
    while True:
        try:
            weight = input('Peso (em kg): ')
            weight = float(weight.replace(',', '.'))
            if weight > 20 and weight < 300:
                break
        except:
            print('Escreva o seu peso em kg')
    return weight

def getage():
    while True:
        try:
            age = int(input('Idade (em anos): '))
            if age > 0:
                break
        except:
            print('Escreva a sua idade em anos')
    return age

def getgender():
    gender = ''
    while (gender not in ('F', 'M')):
        gender = input('Gênero (F ou M): ').upper()
    return gender

def calcTMB(height, weight, age, gender):
    if gender == 'M':
        return (66 + (13.8 * weight) + (5.0 * height) - (6.8 * age))
    elif gender == 'F':
        return (655 + (9.6 * weight) + (1.9 * height) - (4.7 * age))

def boolactive():
    active = ''
    while active not in ('N', 'S'):
        active = input('Você sabe quantas calorias você gasta em um treino ("s" ou "n")? ').upper()
        if active == 'S':
            while True:
                try:
                    active = int(input('Gasto calórico médio em exercicios (em cal): '))
                    if active > 0:
                        break
                except:
                    print('Escreva o seu gasto calórico em cals.')
            return active
        elif active == 'N':
            return False

        
def calcGET(tmb, activety):
    if activety:
        return ((tmb * 1.2) + activety)
    else:
        return (tmb * 1.7)

def calcProtein(weight):
    return (weight*2.5)

def calcFat(weight):
    return weight

main()