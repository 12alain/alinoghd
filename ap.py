import os
import nbformat
import subprocess
from nbformat.v4 import new_notebook , new_code_cell

directory = os.path.join(os.getcwd())

def create_project_structure():

    directory = os.path.join(os.getcwd())
    folders = ["data/raw", "data/cleaned", "docs",
               "models", "notebooks", "reports", "src"]


    for folder in folders:
            
            folder_path = os.path.join(directory, folder)
            os.makedirs(folder_path, exist_ok=True)
            # Crée un fichier .gitkeep dans les dossiers vides pour qu'ils soient suivis
            with open(os.path.join(folder_path, ".gitkeep"), 'w') as f:
                pass

def create_initial_files():

    files = ["LICENSE", "Makefile", "README.md", ".gitignore",
             "requirements.txt"]

    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'w') as f:
            file_content = ''
            f.write(file_content)

def add_specific_files():

    # verifiez si les dossiers existe deja 
    os.makedirs('notebooks', exist_ok=True)
    # Ajoutez une cellule de code au notebook et remplissage du fichier main.ipynb du notebook
    notebook = new_notebook()
    code_source = "print('Hello, world!')"
    cell = new_code_cell(source=code_source)
    notebook.cells.append(cell)
    main_notebook_path = os.path.join(directory, "notebooks/main.ipynb")
    if not os.path.exists(main_notebook_path):
    
        with open(main_notebook_path, "w") as main_notebook_file:
            nbformat.write(notebook,main_notebook_file)
    # ajout du fichier utils.py
    if not os.path.exists("src/utils.py"):
        with open("src/utils.py", "w") as utils_file:
            utils_file.write("")


def commit_changes(commit_message):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])

def make_commits():

    create_project_structure()
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "commit1"])
    subprocess.run(["git", "push", "-u", "origin", "main"])

    create_initial_files()
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "commit2"])
    subprocess.run(["git", "push", "-u", "origin", "main"])

    add_specific_files()
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "commite3"])
    subprocess.run(["git", "push", "-u", "origin", "main"])

    if not os.path.exists("requirement.txt"):
        with open("requirement.txt", "w") as readme_file:
            readme_file.write("#  fichier contenant la liste des dépendances du projets.")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "commite4"])
        subprocess.run(["git", "push", "-u", "origin", "main"])
    if not os.path.exists("LICENCE"):
        with open("LICENCE", "w") as readme_file:
            readme_file.write("les conditons de  lience a lire")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "commite5"])
        subprocess.run(["git", "push", "-u", "origin", "main"])
make_commits()