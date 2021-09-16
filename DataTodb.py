import csv
import pymysql
import requests
import bs4

class DBupload: 
    def __init__(self, dbname):
        self.conn = pymysql.connect(host = 'localhost', user ='root', password = '111111',
                      db = dbname, charset = 'utf8')
        print('DB를 정상적으로 불러왔습니다.')

    def createTable(self, tablename): # make talbe
        with self.conn.cursor() as cur:
            sql = """
            CREATE TABLE IF NOT EXISTS %s (
            code VARCHAR(6),
            date DATE, 
            open bigint(20), 
            high bigint(20),  
            low bigint(20), 
            close bigint(20), 
            diff bigint(20),
            volume bigint(20),
            PRIMARY KEY (code, date))""" % (tablename)

            cur.execute(sql)
            self.conn.commit()      

    def testdata(self):
        with self.conn.cursor() as cur:
            sql_= '''SELECT code FROM company_info;'''
            cur.execute(sql_)
            self.result = cur.fetchall() 
            return self.result                                  

    def importdata(self, start, end, page):

        for i in range(start, end): 
            try:
                url = 'https://finance.naver.com/item/sise_day.nhn?code='f'{self.result[i][0]}&page={page}'
                res = requests.get(url, headers = {'User-agent': 'Mozilla/5.0'})

                bs_obj = bs4.BeautifulSoup(res.content, "html.parser")

                stock_data = bs_obj.find_all("td", {"class" : "num"})
                stock_data_list = [bs_obj.find_all("span")[n].string for n in range(0, len(stock_data) + 11)]
            except:
                pass
            
            k = 1
            try:
                for j in range(0,10):

                    code_ = self.result[i][0]
                    date_ = stock_data_list[k]
                    close_ = int(stock_data_list[k+1].replace(',',''))
                    diff_ = int(stock_data_list[k+2].replace(',',''))
                    open_ = int(stock_data_list[k+3].replace(',',''))
                    high_ = int(stock_data_list[k+4].replace(',',''))
                    low_ = int(stock_data_list[k+5].replace(',',''))
                    vol_ = int(stock_data_list[k+6].replace(',',''))
                            
                    with self.conn.cursor() as cur: #table 명 수정하세요
                        sql = '''insert into dada (code, date, open, high, low, close, diff, volume) values (%s, %s, %s, %s, %s, %s, %s, %s)''' 
                        cur.execute(sql, (code_, date_, open_ , high_, low_, close_, diff_, vol_)) 
                        print('데이터를 보내는중')
                    k += 7
            except:
                return None
        
        self.conn.commit()

A = DBupload('test')

A.testdata()
A.importdata(20,30,1)