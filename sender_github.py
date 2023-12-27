from github import Github
import os

# TODO Criar dag aqui e definir como que realmente vai ficar esse quesito

def enviarParaGithub(file,cidade):

    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo("pibiciot/dataset")
    repo.create_file(file, f"Envio de Arquivo da Cidade {cidade}", "main", branch="test")

enviarParaGithub("main.py")