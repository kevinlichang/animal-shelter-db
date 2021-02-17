import mariadb
import sys
from db_credentials import host, user, passwd, db, port

''' Connects to database and returns database object'''
def connectDB(user = user, passwd = passwd, host = host, port = port, db = db):
    # connection = mariadb.connect(user, passwd, host, port, db)
    try:
        conn = mariadb.connect(
            user=user,
            password=passwd,
            host="localhost",
            port=3306,
            db=db)
        return conn    
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    

'''Executes passed SQL query with passed db connection and returns a Cursor object'''
def executeQuery(dbConnection = None, query = None, query_params = ()):
    if dbConnection is None:
        print("No connection to database")
        return None
    
    if query is None or len(query.strip()) == 0:
        print("Empty query. Please pass a SQL query")
        return None

    #create cursor to execute query
    cursor = dbConnection.cursor()

    '''
    #Create tuple of parameters to send with query
    params = tuple()
    for i in query_params:
        params = params + (i)
    '''

    #Commit changes to database
    cursor.execute(query, query_params)

    # dbConnection.commit()
    return cursor
