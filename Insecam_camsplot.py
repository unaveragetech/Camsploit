
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#github.com/AngelSecurityTeam/Cam-Hackers

import requests, re , colorama ,random
from requests.structures import CaseInsensitiveDict
colorama.init()

url = "http://www.insecam.org/en/jsoncountries/"

headers = CaseInsensitiveDict()
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Host"] = "www.insecam.org"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"


resp = requests.get(url, headers=headers)

data = resp.json()
countries = data['countries']

print("""
\033[1;31m\033[1;37m """
 _____                                                                                                      _____ 
( ___ )                                                                                                    ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                                                      |   | 
 |   |                                                                                                      |   | 
 |   |                                                                                                      |   | 
 |   |         ,gggg,                                                                                       |   | 
 |   |       ,88"""Y8b,                                                   ,dPYb,                   I8       |   | 
 |   |      d8"     `Y8                                                   IP'`Yb                   I8       |   | 
 |   |     d8'   8b  d8                                                   I8  8I             gg 88888888    |   | 
 |   |    ,8I    "Y88P'                                                   I8  8'             ""    I8       |   | 
 |   |    I8'            ,gggg,gg  ,ggg,,ggg,,ggg,     ,g,    gg,gggg,    I8 dP    ,ggggg,   gg    I8       |   | 
 |   |    d8            dP"  "Y8I ,8" "8P" "8P" "8,   ,8'8,   I8P"  "Yb   I8dP    dP"  "Y8ggg88    I8       |   | 
 |   |    Y8,          i8'    ,8I I8   8I   8I   8I  ,8'  Yb  I8'    ,8i  I8P    i8'    ,8I  88   ,I8,      |   | 
 |   |    `Yba,,_____,,d8,   ,d8b,dP   8I   8I   Yb,,8'_   8),I8 _  ,d8' ,d8b,_ ,d8,   ,d8'_,88,_,d88b,     |   | 
 |   |      `"Y8888888P"Y8888P"`Y8P'   8I   8I   `Y8P' "YY8P8PI8 YY88888P8P'"Y88P"Y8888P"  8P""Y88P""Y8     |   | 
 |   |                                                        I8                                            |   | 
 |   |                                                        I8                                            |   | 
 |   |                                                        I8                                            |   | 
 |   |                                                        I8                                            |   | 
 |   |                                                        I8                                            |   | 
 |   |                                                        I8                                            |   | 
 |   |                                                                                                      |   | 
 |   |                                                                                                      |   | 
 |   |                                                                                                      |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                                                    (_____)
"""
\033[1;31m                                                                        INFINIDEV_team \033[1;31m\033[1;37m""")

for key, value in countries.items():
    print(f'Code : ({key}) - {value["country"]} / ({value["count"]})  ')
    print("")



try:
   

    country = input("Code(##) : ")
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    
        with open(f'{country}.txt', 'w') as f:
          for ip in find_ip:
              print("")
              print("\033[1;31m", ip)
              f.write(f'{ip}\n')
except:
    pass
finally:
    print("\033[1;37m")
    print('\033[37mSave File :'+country+'.txt')

    exit()
