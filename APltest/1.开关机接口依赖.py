import requests

#导入库

baseUrl=" https://api.didiyun.com"    #域名
list="/dicloud/i/compute/dc2/list"    #列表接口


guanji="/dicloud/i/compute/dc2/stop"

kaiji="/dicloud/i/compute/dc2/start"

if __name__ == '__main__':

    tou={

        "Accept":"application/json, text/plain, */*",
        "Content-Type":"application/json;charset=UTF-8",
        "Cookie":"Hm_lvt_9eaa41ddde51c419f3c8953af0161d25=1661549247,1661660196,1661660284,1661660530; Hm_lpvt_9eaa41ddde51c419f3c8953af0161d25=1661660693; q=VBT6va1ryeoh4dQvMfjjqPOQyjsLLjN971mffz5GpKckzDuOwzAMANG7TE0YlGhSMtvt9w77cT6NAiRIZfjugZNygMHbGEpik06KMApZhFFJW7S4MIxUYcxkiag13PVoJ_n6RvghQfgle5vNqoYvvS71uP5JcxdWcuNxe97_VtJ34fTWSoS24zuTlB5qvXVrM8Llo15J3V8BAAD__w==; feq=1; u_name=186*****374",
        "Dicloud-Header-Csrf-Token":"uVDTEA4WGpa1yuSNATL1AwW2T_U:1661660700861"

    }
    jiekou1={"start": 0," limit": 10, "simplify": False, "condition": {}}  #数据加上双引号，布偶类型不加双引号首字母大写


    chakan1=requests.post(url=baseUrl+list,json=jiekou1,headers=tou)      #raquests结果 .请求方式  请求需要赋值才能返回数据   有data和json两种  url+l列表，json=数据

    print("第一个请求参数是",chakan1.json)
    jg_json=chakan1.json()


    UUid=jg_json["data"][0]["dc2Uuid"]#dada[0].dc2Uuid
    print(UUid)
#    jiekou2={"dc2": [{"dc2Uuid": "2978abf6a44952abb15a8b70fd191092", "type": "grace"}]}   #关机接口的uid
    jiekou2={"dc2":[{"dc2Uuid":UUid}]}
    chakan2=requests.post(url=baseUrl+kaiji,json=jiekou2,headers=tou)

    print(chakan2.json)



   # time.sleep(10)蛇者睡眠时间
    #print(睡眠结束)

    jiekou3={"dc2":[{"dc2Uuid":UUid}]}

    chakan3=requests.post(url=baseUrl+guanji,json=jiekou3,headers=tou)

    print(chakan3.json())