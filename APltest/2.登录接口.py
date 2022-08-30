

import requests


baseUrl=" https://api.didiyun.com"    #域名
list="/dicloud/i/compute/dc2/list"



tou={

        "Accept":"application/json, text/plain, */*",
        "Content-Type":"application/json;charset=UTF-8",
        "Cookie":"Hm_lvt_9eaa41ddde51c419f3c8953af0161d25=1660678478,1660738417,1661275025,1661469259; Hm_lpvt_9eaa41ddde51c419f3c8953af0161d25=1661469294; feq=1; u_name=186*****374; q=isCT9QCzBrmHQHHqhJZr0sIIL9LTz5wEHiahfP5xZsUkzDmOwkAQQNG7_LhkVXX1Wunkc4dZzJI0EojI8t2RIXzJ25hK4IsuijCNMGEmwodaEaYTKsxMWK1JWx75cCH4-kb4IUD4JXrL7klrGT2NpCr8E-5FWImNx-15_1uJsgun92a5qR3bmcB6Ve-te8sIl896JXR_BQAA__8=",
        "Dicloud-Header-Csrf-Token":"NjxQyxWIwjDBHsJ5Rw-X1MgyauU:1661470140519"

    }
shuju={"start": 0," limit": 10, "simplify": False, "condition": {}}  #数据加上双引号，布偶类型不加双引号首字母大写
chakan=requests.post(url=baseUrl+list,json=shuju,headers=tou)      #raquests结果 .请求方式  请求需要赋值才能返回数据   有data和json两种

print("文本形式查看",chakan.text)
print("json文本查看相应数据",chakan.json())