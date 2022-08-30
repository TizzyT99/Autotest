import requests

url7="http://192.168.8.130/prod-api/getInfo"

tou7={

    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImI2MGM3YmE0LTYyMzktNDBkNi05NmEwLWY2NmMxZmY2MGU4NSJ9.pzvH6i94pVDYAilwO0xe_yju8IQ2lFCjgjQzJm8lm95CXVz487rnJmRHPune5JTNXZf9tUzsIPhxv0WCW0S_gg"
}
res=requests.get(url=url7,headers=tou7)
print(res.json())