# This is a sample Python script.
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import os
from dotenv import load_dotenv

load_dotenv()

cloud_flare_url = 'https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}'

cloud_flare_url_dns_list = 'https://api.cloudflare.com/client/v4/zones/{}/dns_records'

previous_ip = ""


def get_public_ip():
    try:
        r = requests.get('https://ifconfig.me/ip')
        print('public id:', r.text)
        return r.text
    except Exception as e:
        print(e)


def update_cloud_flare(ip: str):
    try:
        DOMAIN_NAME = str(os.getenv("DOMAIN_NAME"))
        ZONE_IDENTIFIER = str(os.getenv("ZONE_IDENTIFIER"))
        API_KEY = str(os.getenv("API_KEY"))

        domain_name = DOMAIN_NAME.split(",")

        headers = {
            "Authorization": "Bearer {}".format(API_KEY),
            "Content-Type": "application/json",
        }
        r_dns_list = requests.get(cloud_flare_url_dns_list.format(ZONE_IDENTIFIER), headers=headers).json()
        dns_list: [] = r_dns_list["result"]
        for dn in domain_name:
            identifier = None
            type_record = None
            proxied = None
            ttl = 3600
            for d in dns_list:
                if d['name'] == dn and (d["type"] == "A" or d["type"] == "AAA"):
                    identifier = d["id"]
                    type_record = d["type"]
                    proxied = d["proxied"]
                    ttl = d['ttl']
            if identifier is None:
                print(dn, "does not exist")
                continue

            body = {
                "content": ip,
                "name": dn,
                "proxied": proxied,
                "type": type_record,
                "comment": "Domain update by ddns service",
                "ttl": ttl
            }
            r = requests.put(cloud_flare_url.format(ZONE_IDENTIFIER, identifier), headers=headers, json=body)
            if r.status_code == 200:
                print("update record:", dn, ip)
                print("response:", r.json())
                print("body:", r.request.body)
                previous_ip = ip
    except Exception as e:
        print(e)


if __name__ == '__main__':
    intervalTime = int(os.getenv("INTERVAL"))
    while True:
        ip = get_public_ip()
        if ip != previous_ip:
            update_cloud_flare(ip)
        else:
            print("IP doesn't change:", ip)
        if intervalTime > 0:
            print("next update:", intervalTime, "minutes")
            time.sleep(intervalTime * 60)
        else:
            print("next update:", 30 , "minutes")
            time.sleep(30 * 60)
