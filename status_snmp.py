import requests
import json


#0.1 - Geração do token
def gera_token():
    values = """
      {
        "data": {
          "username": "admin",
          "password": "admin01"
        }
      }
    """

    headers = {
        'Content-Type': 'application/json'
    }
    request = requests.post('http://10.0.0.1:80/cgi-bin/api/v3/system/login', data=values, headers=headers)

    json_threatment = json.loads(request.text)
    token_code = json_threatment["data"]["Token"]
    return token_code
#Fim 0.1.


#0.2 - Alterando o modo snmp para ativado.
values = """
  {
    "data": {
      "snmp": true,
      "community": "public",
      "port": "161",
      "location": "Right here, Right now",
      "contact": "example@example.org",
      "name": "Wireless Repeater",
      "wan_access": true
    }
  }
"""

headers = {
    'Authorization': 'Token ' + gera_token()
}
request = requests.put('http://10.0.0.1:80/cgi-bin/api/v3/service/snmp', data=values, headers=headers)
#Fim 0.2.

#0.3 - Verificando status snmp
headers = {
    'Authorization': 'Token ' + gera_token()
}
request = requests.get('http://10.0.0.1:80/cgi-bin/api/v3/service/snmp', headers=headers)

print ("Caso o campo snmp :true, o software funcionou", request.text)
#Fim 0.3.