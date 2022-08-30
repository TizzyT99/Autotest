import requests

url3="http://192.168.8.130/prod-api/system/role"#添加角色

tou3={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjdjMjM0NzE0LTk5OTItNDVhZS05NWI3LTQ5NzgzYWU1ODRkOSJ9.E8bPTomYV2cc36g-dQug7p5zwphwOWcSq6YMO1MgZZIVYWXlb2b7ElGSe9TSFPzgZZb6xK7vUaDAUVRx3gPXDQ"


}

shuju3={"roleName":"001","roleKey":"100","roleSort":7,"status":"0","menuIds":[],"deptIds":[],"menuCheckStrictly":False,"deptCheckStrictly":True}
res=requests.post(url=url3,json=shuju3,headers=tou3)
print(res.json())