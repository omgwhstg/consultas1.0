import subprocess
import re
output = subprocess.check_output('ping www.instagram.com', shell=True)



texto = str(output)

endereco_ip = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', texto)[0]
print(endereco_ip)
#import requests
#
#url = f'https://api.apilayer.com/whois/query?domain=instagram.com'
#
#payload = {}
#headers= {
#  "apikey": "iY7nkSQFeAiFSFjTTgLRtovlE7FSLCtd"
#}
#
#response = requests.get(url, headers=headers, data = payload)
#result = response.json()
#print(result)
#print(f'''
#│DOMANAIN NAME :{result["result"]["domain_name"]}
#│WHOIS SERVER :{result["result"]["whois_server"]}
#│REFERRAL URL :{result["result"]["referral_url"]}
#│UPDATED DATE :{result["result"]["updated_date"]}
#│CREATION DATE :{result["result"]["creation_date"]}
#│EXPIRATION DATE :{result["result"]["expiration_date"]}
#│E-MAILS :{result["result"]["emails"]}
#│DNSSEC :{result["result"]["dnssec"]}
#│NAME :{result["result"]["name"]}
#│ORG :{result["result"]["org"]}
#│ADDRESS :{result["result"]["address"]}
#│CITY :{result["result"]["city"]}
#│STATE :{result["result"]["state"]}
#│ZIPCODE :{result["result"]["zipcode"]}
#│COUNTRY :{result["result"]["country"]}
#''')