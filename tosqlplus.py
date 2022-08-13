import time
import pandas as pd
import numpy as np
from numpy import random
import warnings
from sqlalchemy import create_engine
import pymysql
a=time.time()
#建立连接
db = pymysql.connect(host="127.0.0.1", user="root", password="12345", db="natsumei", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor()

sql2="""
update test1 inner join test3 ON test1.index=test3.index set test1.`Factor11`=test3.`Factor11`
"""
sql3="""select * from test1 """

cursor.execute(sql2)
cursor.execute(sql3)
cds = cursor.fetchall()
b=time.time()
df=pd.DataFrame(cds)
print(df)
cursor.close()  # 关闭游标
db.close()  # 关闭数据库连接
print("耗时",b-a)