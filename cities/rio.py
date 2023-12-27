import requests
from utils.saveCityAsCSV import saveCityAsCSV
from utils.convertResponseToDict import convertResponseToDict

def req() -> dict:
    API_URL = "https://jeap.rio.rj.gov.br/dadosAbertosAPI/v2/transporte/veiculos/onibus2"
    response = requests.get(API_URL).json()
    return response 

def process_response(response: dict) -> list:
    # onibus = convertResponseToDict(response, latitude_key='latitude', longitude_key='longitude', tempo_captura_key='dataHora', id_key='ordem')
    # return onibus
    lista_onibus = list()
    for vs in response:
        instancia_processada = {
            'latitude' : vs['latitude'],
            'longitude' : vs['longitude'],
            'tempo_captura' : vs['dataHora'],
            'id_onibus' : vs['ordem']
        }
        lista_onibus.append(instancia_processada)
    return lista_onibus


def rio():
    try:
        response = req()
        processed_response = process_response(response)
        saveCityAsCSV(city="rj", data=processed_response)
    except Exception as e:
        print(f"rio - Error: {e}")
        raise ValueError('Erro em RJ!')

rio()