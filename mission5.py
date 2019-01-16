
# coding: utf-8

# In[ ]:


"""
使用python的request模組去訪問`https://jsonplaceholder.typicode.com/users`  取得第2,3,4,5 筆資料，

偵測當時日期，轉作檔名，將2345筆資料內容寫入檔案中。
"""


# In[3]:


#使用request模組訪問下方網址https://jsonplaceholder.typicode.com/users.

import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')

response = r.json() 


# In[2]:


#取得2-5筆資料
print(response[1:5])


# In[ ]:


#偵測當時日期，新建檔案
nowUtcUnixTime = datetime.datetime.utcnow().timestamp()
print(nowUtcUnixTime)
#轉檔名


# In[ ]:


#將資料建立成檔案

import os
import shutil

fiely = open ( nowUtcUnixTime + '.txt','w')
#將讀出資料寫入檔案
print(response[1:5])

#關閉檔案
fiely.close()


# In[14]:


import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')

response = r.json() 
print(response[1:5])

import datetime
nowTime = datetime.datetime.utcnow().strftime("%Y-%m-%d")
print(nowTime)

#將資料建立成檔案

import os
import shutil

fiely = open(nowTime + ' .txt','w')
#將讀出資料寫入檔案
fiely.write(str(response[1:5]))

#關閉檔案
fiely.close()

