
# coding: utf-8

# In[1]:


get_ipython().system('pip install PyMysql')


# In[2]:



#導入pymysql套件
import pymysql
# 連接database
conn = pymysql.connect(host="mysql.lab", user="root",password="iii",database="mysql",charset="utf8")
# 得到一個可以執行SQL語句的光標對象
cursor = conn.cursor()
# 定義要執行的SQL語句
#創建TABLE 名為USER
#TABLE內容有id欄(自行產生)，name欄(長度限制為10字元，不可空),
#age欄(从 0 到 255 的整型数据。存储大小为 1 字节，不可空<人應該不會超過255歲吧 ?)。
sql = """
CREATE TABLE USER (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
#ENGINE=innodb DEFAULT CHARSET=utf8
#查詢mysql支援的儲存引擎用 InnoDB 其支援transactions 
# 執行SQL語句
cursor.execute(sql)
# 關閉對象
cursor.close()
# 關閉資料庫連接
conn.close()


# In[3]:



#插入資料
# 引入pymysql套件
import pymysql
# 連接database
conn = pymysql.connect(host="mysql.lab", user="root",password="iii",database="mysql",charset="utf8")
# 得到一個可以執行SQL語句的對象
cursor = conn.cursor()
sql = "INSERT INTO USER(name, age) VALUES (%s, %s);"
name = "Guanyebo"
age = 23
# 執行SQL語句
cursor.execute(sql, [name, age])
# 提交事務
conn.commit()
cursor.close()
conn.close()


# In[4]:



#查詢資料
# 引入pymysql套件
import pymysql
# 連接database
conn = pymysql.connect(host="mysql.lab", user="root",password="iii",database="mysql",charset="utf8")
# 得到一個可以執行SQL語句的對象
cur = conn.cursor()
#1.查詢操作  
# 編寫sql 查詢語句  user 對應我的TABLE名  
sql = "SELECT * FROM USER"
try:  
    cur.execute(sql)    #執行sql語句  
  
    results = cur.fetchall()    #獲取查詢的所有記錄  
    print("id","name","age")  
    #遍歷結果  
    for row in results :  
        id = row[0]  
        name = row[1]  
        age = row[2]  
        print(id,name,age)  
except Exception as e:  
    raise e  
finally:  
    conn.close()  #關閉連接 

