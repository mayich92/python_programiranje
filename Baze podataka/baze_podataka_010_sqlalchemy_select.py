import sqlalchemy

db_name = 'Baze podataka/employees.db'
engine = sqlalchemy.create_engine('sqlite:///' + db_name)    # echo=True
db_connection = engine.connect()
db_metadata = sqlalchemy.MetaData()
employees = sqlalchemy.Table('employees', db_metadata, autoload=True, autoload_with=engine)
sql_select_query = sqlalchemy.select([employees])
ResultProxy = db_connection.execute(sql_select_query)
ResultSet = ResultProxy.fetchall()
for result in ResultSet:
    print(result)





