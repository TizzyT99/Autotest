

import requests

url6="http://192.168.8.130/prod-api/system/role/changeStatus"

tou6={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImI2MGM3YmE0LTYyMzktNDBkNi05NmEwLWY2NmMxZmY2MGU4NSJ9.pzvH6i94pVDYAilwO0xe_yju8IQ2lFCjgjQzJm8lm95CXVz487rnJmRHPune5JTNXZf9tUzsIPhxv0WCW0S_gg",
    "Content-Type":"application/json;charset=UTF-8"

}

cs6={"roleId":4,"status":"1"}
res6=requests.put(url=url6,json=cs6,headers=tou6)
print(res6.json())