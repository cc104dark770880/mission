
# coding: utf-8

# In[2]:



get_ipython().system('pip install flask')


# In[ ]:


#引用套件
from flask import Flask, request, abort, jsonify

app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/" )
#給一個可被訪問的路徑/
@app.route('/',methods=['GET'])
#要show出來的內容--以json格式
def hello_world():
    t = {'a':1,'b':'Chicken leg'}
    return jsonify(t)
#啟動程式
if __name__ == "__main__":
    app.run(host='0.0.0.0')

