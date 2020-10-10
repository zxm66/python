#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
import sys 
import requests
import json
import pymysql
 
if __name__ == "__main__":
    conn = pymysql.connect(host='127.0.0.1', user = "root", passwd="root", db="smp_produce", port=3306, charset="utf8")
    cur = conn.cursor()
    sql = "select id,zcaddr,zcname from smp_produce.t_zcinfo where lat is null and lng is null"
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        try:
            # 根据item的address去查经纬度
            url = 'http://api.map.baidu.com/geocoding/v3/?output=json&sn=071c4d942b201cf46aedf59033074c81&callback=showLocation&ak=3Ih4sYMVYhmI6xUmLFc2ROGTs28yN5DK&address='+item[1]
            r = requests.get(url)
            result = json.dumps(str(r.text).replace("showLocation&&showLocation(","").replace(")",""))
            result = json.loads(result)
            location = result.get("result").get("location")
            if location == None:
                #url = 'http://api.map.baidu.com/geocoding/v3/?output=json&sn=071c4d942b201cf46aedf59033074c81&callback=showLocation&ak=3Ih4sYMVYhmI6xUmLFc2ROGTs28yN5DK&address='+item[2] 
                #r = requests.get(url)
                #result = json.dumps(str(r.text).replace("showLocation&&showLocation(","").replace(")",""))
                #result = json.loads(result)
                #location = result.get("result").get("location")
                #lat ,lng = location.get('lat') , location.get('lng')
            # result = json.dumps(result)
            lat ,lng = location.get('lat') , location.get('lng')
            param = tuple([lat,lng,item[0]])
            updateSQL = "update smp_produce.t_zcinfo set lat = %s ,lng = %s  where id = %s"
            cur.execute(updateSQL,param)
            conn.commit()
        except Exception as e:
            pass
        pass
    cur.close()
    conn.close()
 


