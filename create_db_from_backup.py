import os
import glob
import shutil

# Pasta onde os backups estão localizados
backup_folder = "./"

# Lista todos os arquivos de backup na pasta
backup_files = glob.glob(os.path.join(backup_folder, "backup_*.db"))

# Verifica se há algum backup disponível
if backup_files:
    # Pega o arquivo mais recente (último backup criado)
    latest_backup = max(backup_files, key=os.path.getctime)

    # Define o nome para a cópia como 'db.sqlite3'
    new_filename = os.path.join(backup_folder, "db.sqlite3")

    # Cria uma cópia do arquivo de backup com o nome 'db.sqlite3'
    shutil.copy2(latest_backup, new_filename)

    print("Cópia do backup criada como db.sqlite3")
else:
    print("Nenhum backup encontrado na pasta.")
