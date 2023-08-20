import json
import requests

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "2eb64fc364e0ec81d7a54cccbbcb4723",
    "redirect_url" : "http://101.101.211.68",
    "code" : "q8s6BH3KPtJXT2K7l7MrBwN7GtYvmCtIMDt8pZljfpEL3CX8hFWhFQngbqXj9UYrhClopwo9c04AAAGKEfB1sw"
}
response = requests.post(url, data=data)
tokens = response.json()

with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + "ki6sZgM8kZX7ZJXYgj1PTR0PMZNK1Uet4l_BPGpDCisNIAAAAYoR8XI6"
}
data = {
    "template_object" : json.dumps({ "object_type" : "text",
        "text" : "이름 : 이은지 이런이런 내용으로 상담문의 드립니다 연락부탁드립니다.",
        "link" : {
        "mobile_web_url" : "http://101.101.211.68"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
