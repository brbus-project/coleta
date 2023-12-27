from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

def auth():
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("/home/felipe/airflow/dags/utils/mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("/home/felipe/airflow/dags/utils/mycreds.txt")

    return gauth

def runUpload(city,file):
    gauth = auth()
    drive = GoogleDrive(gauth)
    archive_name = file.split("/")[-1]
    path = "/home/felipe/airflow/dags/arquivos"
    idDict = {"sp":"1Gk6NIyt6MDHQiAiyz3fLJj9DfOpMiXH5",
              "rj":"1NiuzubQ9NiOS4idhUXle4O7tix-mg6fi",
              "cwb":"1CuFqsvCJEEV628RP-AC1FwVh8uA0GvCX",
              "df":"17G9VsEJPCMznOFiwTJgvvsrEjzz83h9K"
              }
    
    # archive_path = shutil.make_archive(archive_name, compression_format, 'dataset')
    gfile = drive.CreateFile({'parents': [{'id': idDict[city]}],'title':archive_name}) # id of the folder in which you want to upload
    try:
        gfile.SetContentFile(f"{path}/{city}/{archive_name}")
    except:
        pass
    gfile.Upload()

# auth()

# def backup():
#     try:
#         file = open("",'r')
#         city,filename = file.readline().split(',')
#         runUpload(city,filename)
#         file.close()
#     except:
#         raise ValueError(f'Erro no Backup!')
    

def backup():
    try:
        file = open("/home/felipe/airflow/dags/cities/temp_file.txt",'r')
        text = file.readlines()
        print(text)
        for x in text:
            city,filename = x.split(",")
            filename = filename.replace("\n","")
            runUpload(city,filename)
        file.close()
    except:
        raise ValueError(f'Erro em no Backup!')


def cleanfile():
    with open(r"/home/felipe/airflow/dags/cities/temp_file.txt", 'r+') as fp:
        # read an store all lines into list
        # lines = fp.readlines()
        # move file pointer to the beginning of a file
        fp.seek(0)
        # truncate the file
        fp.truncate()

backup()
cleanfile()