# Version 1 : lire un fichier de logs et afficher les échecs SSH

with open("auth_test.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            print(line.strip())
