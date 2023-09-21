
import oracledb

conn = oracledb . connect ( 
    user ='rm552283', 
    password ='170204', 
    dsn ='oracle.fiap.com.br/orcl ')

print("Versao do banco", conn.version)

cur = conn.cursor()
cur.execute("select * from empregad")

cur = conn . cursor () # Criar um cursor
cur . execute ('SELECT * FROM EMPREGADO ')

rows = cur . fetchall ()
for reg in rows : print ( reg )

cur . close ()
conn . close ()