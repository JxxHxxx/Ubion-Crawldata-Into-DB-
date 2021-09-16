import pandas as pd
import pymysql

class DBupdate:
    def __init__(self):
        self.conn = pymysql.connect(host = 'localhost', user ='root', password = '111111',
                        db = 'titanic', charset = 'utf8')

    def createTable(self):
        with self.conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS titanic (sex CHAR(6) , \
                                                            age FLOAT(6), \
                                                            embarked CHAR(1))") 
        
        self.conn.commit()

    def DataToDB(self):

        titanic = pd.read_csv('train.csv')
        titanic = titanic[['Sex','Age','Embarked']]
        titanic['Age'] = titanic['Age'].fillna(titanic['Age'].mean())
        titanic['Embarked'] = titanic['Embarked'].fillna('Q')
        
        with self.conn.cursor() as cur:
            for i in range(len(titanic['Sex'])): 
                col1 = titanic['Sex'][i]
                col2 = titanic['Age'][i] 
                col3 = titanic['Embarked'][i] 
                sql = '''insert into titanic (sex, age, embarked) values (%s, %s, %s) ; '''
                cur.execute(sql, (col1, col2, col3))                          
        self.conn.commit()

titanicDB = DBupdate()
titanicDB.createTable()
titanicDB.DataToDB()
