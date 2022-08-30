import requests

url1="http://192.168.8.130/prod-api/system/role"

cs1={

    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjdjMjM0NzE0LTk5OTItNDVhZS05NWI3LTQ5NzgzYWU1ODRkOSJ9.E8bPTomYV2cc36g-dQug7p5zwphwOWcSq6YMO1MgZZIVYWXlb2b7ElGSe9TSFPzgZZb6xK7vUaDAUVRx3gPXDQ",
    "Content-Type":"application/json;charset=UTF-8"
}

shuju1={"searchValue":None,"createBy":None,"createTime":"2022-08-27 14:51:09","updateBy":None,"updateTime":None,"remark":None,"params":{},"roleId":5,"roleName":"003","roleKey":"000","roleSort":6,"dataScope":"1","menuCheckStrictly":False,"deptCheckStrictly":True,"status":"0","delFlag":"0","flag":False,"menuIds":[],"deptIds":None,"admin":False}
res=requests.put(url=url1,json=shuju1,headers=cs1)
print(res.json())