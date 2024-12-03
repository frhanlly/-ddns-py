#!/bin/python3
import requests as re
import json, os
from dotenv import load_dotenv

load_dotenv()


API_TOKEN=os.getenv('API_TOKEN')
ZONE_ID=os.getenv('ZONE_ID')
DNS_ID=os.getenv('DNS_ID')

DNS_ENTRY=os.getenv('DNS_ENTRY')
DNS_TYPE=os.getenv('DNS_TYPE')


API_ENDPOINT_GETDNS=f'https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records'
API_ENDPOINT_PATCHDNS=f'https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{DNS_ID}'
GETIP_ENDPOINT='https://ifconfig.me'

headers = {
    'Authorization': f'Bearer {API_TOKEN}'
}


res_dict = json.loads(re.get(f'{API_ENDPOINT_GETDNS}', headers=headers).text)
res_dict_result = res_dict['result']

filered_res_dict = filter(lambda dns: dns.get('name') == f'{DNS_ENTRY}' and 
                          dns.get('type') == f'{DNS_TYPE}', res_dict_result)

last_ipv4 = list(filered_res_dict)[0].get('content')
current_ipv4=re.get(f'{GETIP_ENDPOINT}').text


if(last_ipv4 != current_ipv4):
    req_body = {
        "content": current_ipv4
    }
    res = re.patch(f'{API_ENDPOINT_PATCHDNS}', headers=headers, json=req_body)
    
    if res.status_code >= 200 and res.status_code < 300:
        print('FEITO UPDATE DO DNS...')
    



