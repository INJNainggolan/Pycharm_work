'''
# -*- coding: utf-8 -*-
import requests
import csv
import os


base_url = 'https://m.weibo.cn/api/comments/show?id=4131150395559419&page={page}'
cookies = {'Cookie':'YF-V5-G0=4955da6a9f369238c2a1bc4f70789871; login_sid_t=b4e6baaac372a7b911dc26f8e42072a5; cross_origin_proto=SSL; YF-Ugrow-G0=ad83bc19c1269e709f753b172bddb094; _s_tentry=passport.weibo.com; Apache=8079212709090.753.1517804459883; SINAGLOBAL=8079212709090.753.1517804459883; ULV=1517804459889:1:1:1:8079212709090.753.1517804459883:; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWluYr8i_l9EcgML.PIyGFK5JpX5KzhUgL.Foz4eoB7Sh-7SK-2dJLoIp9gqg4ki--Ni-82i-27i--NiK.7i-z7; SUHB=0u5RbLKPLe7epO; ALF=1549340467; SSOLoginState=1517804467; wvr=6; wb_cusLike_2924045055=N; YF-Page-G0=ab26db581320127b3a3450a0429cde69'}
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'}

path = os.getcwd()+"/weibo.csv"
csvfile = open(path, 'a+', encoding='utf-8',newline='')
writer = csv.writer(csvfile)
writer.writerow(('username','source','comment'))

for i in range(0,83):
    try:
        url = base_url.format(page=i)
        resp = requests.get(url, headers=headers, cookies=cookies)
        jsondata = resp.json()

        data = jsondata.get('data')
        for d in data:
            created_at = d.get("created_at")
            source = d.get("source")
            username = d.get("user").get("screen_name")
            comment = d.get("text")
            print((username,source,comment))
            writer.writerow((username, source, comment))
    except:
        print('*'*1000)
        pass

csvfile.close()
'''
# -*- coding: utf-8 -*-
import requests
import csv
import os


base_url = 'https://m.weibo.cn/api/comments/show?id=4175373614478883&page=100'
cookies = {'Cookie':'ALF=1515398343; SCF=Aj-rqiCj-NMb0O5CGH_UAEK7kFwX-_H4G-2q5jWYFhrK56eojPtG8zpgeu653p2fL9Wdy9GM4dRNLmRbGtlt9fI.; SUB=_2A253L-eYDeRhGeVO6FMW8S3IyzuIHXVU04nQrDV6PUNbktBeLXL7kW1NTTSv4TVIaQGEaS3sje_0E1dOA7HMyE-F; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5yKaZgr_wG4qPXjhULDBhp5JpX5KMhUgL.Foe7e02NeKeXehM2dJLoIEqLxKqL1KnL1-qLxKMLBK.LB.2LxKqLBKzLBKqLxKnL1-BLBo9Ad5tt; SUHB=0ebddz7UBJ8UXK; _T_WM=56c009308dee081acf0177902ef81f4e; SSOLoginState=1512806344; M_WEIBOCN_PARAMS=lfid%3D1076031632843173%26featurecode%3D20000320%26luicode%3D10000370; H5:PWA:UID=1; H5_INDEX=2; H5_INDEX_TITLE=%E6%98%9F%E7%A9%BA%E6%A2%A6%E8%9D%B6zl'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

path = os.getcwd()+"/weibo.csv"
csvfile = open(path, 'a+', encoding='utf-8',newline='')
writer = csv.writer(csvfile)
writer.writerow(('username','source','comment'))

for i in range(1,100):
    try:
        url = base_url.format(page=i)
        resp = requests.get(url, headers=headers, cookies=cookies)
        jsondata = resp.json()

        data = jsondata.get('data')
        for d in data:
            created_at = d.get("created_at")
            source = d.get("source")
            username = d.get("user").get("screen_name")
            comment = d.get("text")
            print((username,source,comment))
            writer.writerow((username, source, comment))
    except:
        print('*'*1000)
        pass

csvfile.close()
