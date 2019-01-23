
# coding: utf-8

# In[1]:


get_ipython().system('pip install boto3')


# In[2]:



#連線 dynamodb 
#引用套件
import boto3

dynamodb = boto3.resource(

    'dynamodb',

    endpoint_url='http://dynamodb.local:8000',   #連線網址192.168.254.100:8000 虛機ip位址，在虛機內開8

    region_name='dummy_region',                   #區域名稱 選用虛擬區域

    aws_access_key_id='dummy_access_key',         #aws進入鑰匙id選用虛擬進入key

    aws_secret_access_key='dummy_secret_key',     #aws私鑰選用虛擬私鑰進去

    verify=False)                                 #是否去认证ssl证书，默认SSL证书需要认证，設定verify=False不去认证SSL证书的有效性


# In[3]:



#創建資料表
import boto3
#創建table
create_table = dynamodb.create_table(
    TableName='cc104',
       KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'   #主key
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE' #sortkey
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 50,
        'WriteCapacityUnits': 50
    }
)
#等待binghongtable 創建好 
create_table.meta.client.get_waiter('table_exists').wait(TableName='cc104')

# 計算cc104 table的物件數

print(create_table.item_count)


# In[31]:



#引用套件
import boto3
#插入資料
dynamodb2 = boto3.resource(

    'dynamodb',

    endpoint_url='http://dynamodb.local:8000',   #連線網址192.168.254.100:8000 虛機ip位址，在虛機內開8

    region_name='dummy_region',                   #區域名稱 選用虛擬區域

    aws_access_key_id='dummy_access_key',         #aws進入鑰匙id選用虛擬進入key

    aws_secret_access_key='dummy_secret_key',     #aws私鑰選用虛擬私鑰進去

    verify=False)    
table = dynamodb2.Table('cc104')

print('beforeput:', table.item_count)
#插入資料
table.put_item(
     Item={
        'username': 'apple2',
        'last_name': 'banana',
        'age': 30,
        'account_type': 'standard_user'
         }
            )

print('afterput:', table.item_count)


# In[35]:


table = dynamodb2.Table('cc104')
print (table) 


# In[42]:


#引用套件
import boto3
    #查詢資料
reeponse = table.get_item(
        Key={
           'username': 'apple2',
           'last_name': 'banana'
       }
)
item = reeponse['Item']
print(item)


# In[41]:


#引用套件
import boto3
#更新物件  
table.update_item(
     Key={
        'username': 'apple2',
        'last_name': 'banana'
     },
    
     UpdateExpression='SET age = :val1',  #更新表達式

     ExpressionAttributeValues={          #表達式屬性值

        ':val1': 60
    }


)


# In[43]:


#引用套件
import boto3
    #查詢資料
reeponse = table.get_item(
        Key={
           'username': 'apple2',
           'last_name': 'banana'
       }
)
item = reeponse['Item']
print(item)


# In[44]:



#引用套件
import boto3
#刪除資料
print('beforedelete:', table.item_count)
table.delete_item(
    Key={
        'username': 'apple',
        'last_name': 'banana'
    }
)
print('afterdelete:', table.item_count)


# In[45]:



#引用套件
import boto3
#刪除資料
print('beforedelete:', table.item_count)
table.delete_item(
    Key={
        'username': 'apple2',
        'last_name': 'banana'
    }
)
print('afterdelete:', table.item_count)


# 
# 
# dsadadawdad
# 
# 
# 
# 
# 
# 
# #### 
