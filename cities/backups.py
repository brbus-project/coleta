
from utils import upload

def backup():
    try:
        file = open("temp_file.txt",'r')
        text = file.readlines()
        for x in text:
            city,filename = x.split(",")
            filename = filename.replace("\n","")
            upload(city,filename)
        file.close()
    except:
        raise ValueError(f'Erro em no Backup de {city}!')
