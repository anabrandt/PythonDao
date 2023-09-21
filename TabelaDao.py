
import oracledb

con = oracledb . connect ( 
    user ='rm552283', 
    password ='170204', 
    dsn ='oracle.fiap.com.br/orcl ')

print("Versao do banco", con.version)

cur = con.cursor()
cur.execute("select * from empregad")

cur = con . cursor () # Criar um cursor
cur . execute ('SELECT * FROM EMPREGADO ')


cur . close ()
con . close ()