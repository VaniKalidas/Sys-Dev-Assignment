from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QTableView, QApplication
import sys
from globals import dbinfo

def crtCnnSql(server,database,uid,pwd,cnx_nbr):
    ''' Connect to a SQL Server instance using SQl Server authentication '''
    db = QSqlDatabase.addDatabase('QODBC',str(cnx_nbr))          
    connString = f'DRIVER={{SQL Server}};'\
                f'SERVER={server};'\
                f'DATABASE={database};'\
                f'UID={uid};'\
                f'PWD={pwd}'
    #print(connString)
    db.setDatabaseName(connString)
    dbinfo.cnx_nbr += 1

    if db.open():
        dbinfo.cnx_nbr += 1
        #print('connect to SQL Server successfully')
        return db
    else:
        #print('connection failed')
        return db
    
def chkSqlUsr(server,database,uid,pwd):
    ''' Checks username and password using SQL Server Auth.
        Used by Login screen to check credentials
        Does not return a connection.'''
    db = QSqlDatabase.addDatabase('QODBC',str(dbinfo.cnx_nbr))          
    connString = f'DRIVER={{SQL Server}};'\
                f'SERVER={server};'\
                f'DATABASE={database};'\
                f'UID={dbinfo.adminuser};'\
                f'PWD={dbinfo.adminpwd}'
    print(connString)
    db.setDatabaseName(connString)
    dbinfo.cnx_nbr += 1
    # print(db)
    if db.open():
        qry = QSqlQuery(db)
        sql_statement = f'SELECT * from Users WHERE UserName = \'' \
                        f'{uid}\'' \
                        f' AND UserPwd = \'' \
                        f'{pwd}\' '

        print(sql_statement)
        qry.prepare(sql_statement)
        #print('query running')
        qry.exec()
        if qry.first():
            qry.finish()
            db.close
            return True
       #print('connect to SQL Server successfully')
        else:
            qry.finish()
            db.close
            return False
       #print('connection failed')        

def displayData(sqlStatement):
    ''' Only used when called as script '''
    #print('processing query...')
    qry = QSqlQuery(db)
    qry.prepare(sqlStatement)
    qry.exec()

    model = QSqlQueryModel()
    model.setQuery(qry)

    view = QTableView()
    view.setModel(model)
    return view    

if __name__=='__main__':
    #db = QSqlDatabase.addDatabase('QODBC',"sourcedata1")
    #SERVER_NAME = '213.171.218.230'
    #DATABASE_NAME = 'sourcedata1'
    #USERNAME = 'ECM1420_DBO'
    #PASSWORD = 'Holsworthy99*'
    driver = 'SQL Server'
     
    dbinfo.database = 'HR'
    dbinfo.username = 'hrtest'
    dbinfo.password = 'hrtest'
    #print('Connection number: ', dbinfo.cnx_nbr)
    app = QApplication(sys.argv)

    db = crtCnnSql(dbinfo.server,dbinfo.database,dbinfo.username,dbinfo.password,dbinfo.cnx_nbr)
    #print(cnx.DatabaseName)
    if db.open():
        sql_statement = "SELECT ProjectId, Name, StartDate, Budget FROM project"
        dataView = displayData(sql_statement)
        dataView.show()
                  
    app.exit()
    sys.exit(app.exec_())