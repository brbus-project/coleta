import time
import pandas as pd
import os

def saveCityAsCSV(city, data):
    timestamp = str(time.time())
    try:
        df = pd.DataFrame(data)
        dataset_dir = '/home/felipe/airflow/dags/arquivos'
        output_dir = f"{dataset_dir}/{city}"

        if not os.path.exists(f"{dataset_dir}/{city}"):
            os.makedirs(f"{dataset_dir}/{city}")

        df.to_csv(f"{output_dir}/{timestamp}.csv")

        with open("/home/felipe/airflow/dags/cities/temp_file.txt", 'a') as fp:
            text = f"{city},{timestamp}.csv\n"
            fp.writelines(text)

        print(f"SAVING FILE {city}")
    except Exception as e:
        print(f"{city} - Error on save as CSV {timestamp}: {e}")

