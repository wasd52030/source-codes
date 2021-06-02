import requests
import pymysql
import sqlconfig

res = requests.get('https://apis.youbike.com.tw/api/front/station/all?lang=tw&type=2')

rd = res.json()['retVal']
title = [f'`{x}`' for x in rd[0].keys()]
d = [list(i.values()) for i in rd]

#創資料表，在創建時同時檢查資料表是否已存在
crtable = 'CREATE TABLE IF NOT EXISTS `n`.`ybk` ('
crtable += ' VARCHAR(100) NOT NULL, '.join(title)
crtable += ' VARCHAR(100) NOT NULL, PRIMARY KEY (`station_no`)) ENGINE = InnoDB;'

#插入資料
insert = "INSERT INTO `ybk` (`country_code`, `area_code`, `type`, `status`, `station_no`, `name_tw`, `district_tw`, `address_tw`, `name_en`, `district_en`, `address_en`, `name_cn`, `district_cn`, `address_cn`, `parking_spaces`, `available_spaces`, `empty_spaces`, `forbidden_spaces`, `lat`, `lng`, `img`, `updated_at`, `time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

try:
    conn = pymysql.connect(**sqlconfig.dbConfig)
    with conn.cursor() as cur:
        cur.execute(crtable)
        print('table has been created')

    with conn.cursor() as cur:
        for i in d:
            cur.execute(insert, i)
            conn.commit()
        print('data has been inserted')
except Exception as e:
    print(e)
