
# coding: utf-8

# In[1]:


get_ipython().system('pip install flask')


# In[ ]:


#引用套件
from flask import Flask, request, abort, jsonify
#增加flask這個app的啟動點
app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/" )
#給一個可被訪問的路徑/
@app.route('/',methods=['GET'])
def hello_world():
 #取用用戶的querystring
       #192.168.50.195:5000?id=123
       #遇到get使用id存取時的值=t
    t = request.args.get('id')
      #轉成Dict
    jsonDict = {'userId':t}
      #轉成json並回傳在網頁上
    return jsonify(jsonDict)
    #啟用伺服器
if __name__ == "__main__":
    app.run(host='0.0.0.0')

