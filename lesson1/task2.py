country = {
    'UA' : 'Kiev',
    'RU' : 'Moscow',
    'EU' : 'Eureop'
}

q = ('UA', 'RU', 'GR')

for item in q:

    if item in country:
        print(country[item])
    else:
        print('Country dose not exist')