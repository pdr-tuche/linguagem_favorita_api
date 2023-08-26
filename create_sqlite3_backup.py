import shutil
import sqlite3
import datetime

# Caminho para o arquivo do banco de dados original e para o backup
db_file = "./db.sqlite3"
backup_file = f"backup_{datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')}.db"

# Copiando o arquivo do banco de dados para criar o backup
shutil.copy2(db_file, backup_file)

print(f"Backup criado: {backup_file}")
