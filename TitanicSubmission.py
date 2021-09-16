import pandas as pd
import pymysql

def connectionDB():
    conn = pymysql.connect(host = 'localhost', user ='root', password = '111111',
                      db = 'shoppingdb', charset = 'utf8')

    return conn

def importData():
    titanic = pd.read_csv('train.csv') # 데이터를 불러옵니다.
    titanic = titanic[['Sex','Age','Embarked']] # DB에 집어넣은 컬럼(속성)들만 불러옵니다.
    titanic['Age'] = titanic['Age'].fillna(titanic['Age'].mean()) # Null 값을 Age의 평균, Embarked 의 Q로 대체합니다.
    titanic['Embarked'] = titanic['Embarked'].fillna('Q')

def createDbTable():
    conn = connectionDB()
    with conn.cursor() as cur:
        #cur.execute("CREATE DATABASE IF NOT EXISTS titanic") # titanic Database을 만듭니다.
        cur.execute("USE titanic") # titanic Database 를 사용합니다.
        cur.execute("CREATE TABLE IF NOT EXISTS titanic (sex CHAR(8) , age FLOAT(16),embarked CHAR(2))") 
# titanic Database 에 titanic Table 을 생성합니다.

def DataToDB():
    titanic = importData()
    conn = connectionDB()

    with conn.cursor() as cur:
        for i in range(len(titanic['Sex'])): 
            col1 = titanic['Sex'][i] # i 번째 탑승자의 성별
            print('%d 번째 탑승자의 성별 : %s 입니다. Titanic DB 에 정보를 저장합니다.' % (i + 1 ,col1))
            col2 = titanic['Age'][i] # i 번째 탑승자의 나이
            print('%d 번째 탑승자의 나이 : %s 입니다. Titanic DB 에 정보를 저장합니다.' % (i + 1,col2)) 
            col3 = titanic['Embarked'][i] # i 번째 탑승자의 탑승지
            print('%d 번째 탑승자의 탑승지 : %s 입니다. Titanic DB 에 정보를 저장합니다.' % (i + 1,col3))
            
            sql = '''insert into titanic (sex, age, embarked) values (%s, %s, %s) ; ''' # mysql query
            cur.execute(sql, (col1, col2, col3))        # 실행                                 
            print('타이타닉 탑승자 한 명의 정보가 정상적으로 들어갔습니다.')
        conn.commit() # 저장

connectionDB()
importData()
DataToDB()