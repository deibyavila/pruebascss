paises = {
    'colombia':49,
    'mexico':122
}

while True:
    pais = str(input('ecsibra un pais: ')).lower()
    try:
        print('la poblacion de {} es de {}'.format(pais, paises[pais]))
    except KeyError:
        print('pailas no se entro resultado')
    finally:
        print('fin de busqueda')
    