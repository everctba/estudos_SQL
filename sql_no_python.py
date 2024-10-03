import sqlite3

connect = sqlite3.connect("I:\P\projetos-ever\SQL\estudos_SQL\primeiro_teste_primeiro_banco.db")

cursor = connect.cursor()



cursor.close()
connect.close()

