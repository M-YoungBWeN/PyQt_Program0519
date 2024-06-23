"""
官方接口文档
https://eco.dameng.com/document/dm/zh-cn/pm/dmpython-interface.html
"""
import dmPython

# 建立接口
conn = dmPython.connect(user='SYSDBA', password='SYSDBA', server='localhost',
                        port=5236, autoCommit=True)
# 创建游标
cursor = conn.cursor()
# 对数据库进行操作
cursor.execute('SELECT * FROM "TEST0623"."all_weapons_with_types";')
values = cursor.fetchall()
print(values)
# 关闭游标和接口
cursor.close()
conn.close()
