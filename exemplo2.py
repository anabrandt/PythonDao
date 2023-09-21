import oracledb

with oracledb.connect( user='rm552283', 
                      password="170204", 
                      dsn='oracle.fiap.com.br') as con:
    
    with con.cursor() as cur:
        dado= {
            'num':10, 'nome': 'Prof Pardal',
            'sal': 8500, 'deoartamento': 'PAD'}
        sql = ''' update emprego set nome =: nome,
        salario =: sal,
        departamento=: departamento where numero=:num'''
        cur.execute(sql,dado)
        con.commit()