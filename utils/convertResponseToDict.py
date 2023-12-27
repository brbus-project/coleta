def convertResponseToDict(response, latitude_key, longitude_key, tempo_captura_key, id_key):
    lista_onibus = list()
    for vs in response:
        instancia_processada = {
            'latitude' : vs[latitude_key],
            'longitude' : vs[longitude_key],
            'tempo_captura' : vs[tempo_captura_key],
            'id_onibus' : vs[id_key]
        }
        lista_onibus.append(instancia_processada)
    return lista_onibus