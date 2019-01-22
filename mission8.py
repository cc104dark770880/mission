
# coding: utf-8

# In[2]:


get_ipython().system('pip install flask')


# In[4]:


get_ipython().system('pip install boto3')


# In[6]:


get_ipython().system('pip install boto3 awscli')


# In[ ]:



from flask import Flask, request, jsonify
import boto3
from pprint import pprint
import os
import shutil
#flask這個應用的啟動點
app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/" )
#為這個啟動點增加訪問路徑'/' ,使用post方法訪問
@app.route('/',methods=['POST'])
def leg():
    t =request.get_json()
    #取得用戶json的nickname,並且組成{'nickname':'xxxxxx'}
    jsonDict = {'binghong':t.get('binghong','eat Chicken leg!!!!')}
    getbody = str(jsonDict)
    # 開起一個檔案，寫入，關閉 
    missionFile = open('mission8.txt','w')
    missionFile.write(getbody)
    missionFile.close()   
    #上傳到S3中-----------------------------
    #啟用s3客戶端
    s3resource = boto3.resource('s3')
    #使用s3客戶端上傳檔案(step1-s3-demo.txt)到s3的butket(iii-tutorial-v2下的student9裡)
    uploadObject = s3resource.Object('iii-tutorial-v2', 'student9/mission8.txt').put(Body=open('./mission8.txt', 'rb'))
    pprint(uploadObject)
    #瀏覽s3的butket(iii-tutorial-v2下的student9裡內的物件)
    print("=============上傳成功================")
    return "update ok"
if __name__ == "__main__":
    app.run(host='0.0.0.0')

