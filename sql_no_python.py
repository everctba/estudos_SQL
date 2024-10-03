import sqlite3

connect = sqlite3.connect("I:\P\projetos-ever\SQL\estudos_SQL\tete_primeiro_banco.db")

cursor = connect.cursor()



cursor.close()
connect.close()

