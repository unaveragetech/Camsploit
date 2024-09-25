#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# github.com/AngelSecurityTeam/Cam-Hackers

import requests
import re
import colorama
from requests.structures import CaseInsensitiveDict

colorama.init()

url = "http://www.insecam.org/en/jsoncountries/"

# Setting headers for the requests
headers = CaseInsensitiveDict({
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.insecam.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
})

# Fetching country data
try:
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()  # Raise an error for bad responses
    data = resp.json()
    countries = data['countries']

    print("""
\033[1;31m\033[1;37m
   (                             (             )  
   )\      )     )               )\     (   ( /(  
 (((_)  ( /(    (     (   `  )  ((_) (  )\  )\()) 
 )\___  )(_))   )\  ' )\  /(/(   _   )\((_)(_))/  
((/ __|((_)_  _((_)) ((_)((_)_\ | | ((_)(_)| |_   
 | (__ / _` || '  \()(_-<| '_ \)| |/ _ \| ||  _|  
  \___|\__,_||_|_|_| /__/| .__/ |_|\___/|_| \__|  
                         
\033[1;31m 
\033[1;31m   Infinidev Team \033[1;31m\033[1;37m""")

    for key, value in countries.items():
        print(f'Code : ({key}) - {value["country"]} / ({value["count"]})')
        print("")

    country = input("Code(##): ")
    res = requests.get(f"http://www.insecam.org/en/bycountry/{country}", headers=headers)
    res.raise_for_status()  # Raise an error for bad responses
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    with open(f'{country}.txt', 'w') as f:
        for page in range(int(last_page)):
            res = requests.get(f"http://www.insecam.org/en/bycountry/{country}/?page={page}", headers=headers)
            res.raise_for_status()  # Raise an error for bad responses
            find_ip = re.findall(r"http://\d+\.\d+\.\d+\.\d+:\d+", res.text)

            for ip in find_ip:
                print("\033[1;31m", ip)
                f.write(f'{ip}\n')

except requests.exceptions.RequestException as e:
    print(f"\033[1;31mError: {e}\033[0m")
except IndexError:
    print("\033[1;31mError: No pages found for the specified country.\033[0m")
except Exception as e:
    print(f"\033[1;31mAn unexpected error occurred: {e}\033[0m")
finally:
    print("\033[1;37m")
    print(f'Save File: {country}.txt' if 'country' in locals() else "No country selected.")
