import requests
from utils.saveCityAsCSV import saveCityAsCSV

def req():
    API_URL = "https://www.sistemas.dftrans.df.gov.br/service/gps/operacoes"
    response = requests.get(API_URL).json()
    return response

def process_response(response: dict) -> list:
    lista_onibus= list()
    for operadora in response:
        for vs in operadora['veiculos']:
            instancia_processada = {
                'latitude': vs['localizacao']['longitude'],
                'longitude': vs['localizacao']['latitude'],
                'tempo_captura': vs['horario'],
                'id_onibus': vs['numero']
            }
            lista_onibus.append(instancia_processada)
    return lista_onibus

def df():
    try:
        response = req()
        processed_response = process_response(response)
        saveCityAsCSV(city="df", data=processed_response)
    except Exception as e:
        print(f"distrito_federal - Error: {e}")
        raise ValueError('Erro em DF!')

df()