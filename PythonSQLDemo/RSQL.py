import json
import pymysql
import sqlconfig

try:
    conn = pymysql.connect(**sqlconfig.dbConfig)
    query = 'SELECT * FROM `ybk`'
    with conn.cursor() as cur:
        cur.execute(query)

        #取資料表欄位名
        rkey = [des[0] for des in cur.description]

        #取資料表欄位資料
        rval = [list(i) for i in cur.fetchall()]

        #組成dict list並轉成json
        # zip(a,b) => 分別將所傳入的兩個可迭代元素中取位置對應的元素，組成一truple並回傳，回傳值可轉成list、dict...等
        dJson = json.dumps([dict(zip(rkey, i)) for i in rval], indent=4, ensure_ascii=False)
        
        print(dJson)
except Exception as e:
    print(e)
