
import requests



url2= "http://192.168.8.130/prod-api/system/user"#添加用户

tou2={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjdjMjM0NzE0LTk5OTItNDVhZS05NWI3LTQ5NzgzYWU1ODRkOSJ9.E8bPTomYV2cc36g-dQug7p5zwphwOWcSq6YMO1MgZZIVYWXlb2b7ElGSe9TSFPzgZZb6xK7vUaDAUVRx3gPXDQ",
    "Content-Type":"application/json;charset=UTF-8"

}
shuju2={"userName":"666","nickName":"666","password":"123456","status":"0","postIds":[],"roleIds":[]}
res=requests.post(url=url2,json=shuju2,headers=tou2)
print(res.json())