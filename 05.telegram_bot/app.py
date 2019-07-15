from flask import Flask, request, render_template
from decouple import config
import requests
import random
from bs4 import BeautifulSoup
import csv

app = Flask(__name__)

api_url = "https://api.telegram.org"
token = config("TELEGRAM_TOKEN")
chat_id = config("CHAT_ID")
naver_id = config("NAVER_ID")
naver_secret = config("NAVER_SECRET")
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello,'

@app.route("/write")
def write():
    return render_template("write.html")

@app.route("/send")
def send():
    msg = request.args.get('msg')
    url = f"{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    res = requests.get(url)
    return render_template("send.html")

@app.route(f"/{token}", methods=['POST'])
def telegram():
    print(request.get_json())
    data = request.get_json()
    user_id = data.get('message').get('from').get('id')
    user_msg = data.get('message').get('text')

    if data.get('message').get('photo') is None:

        if user_msg == "오늘 뭐먹지":
            menu_list = ['맹물','있는거','굶기']
            result = random.choice(menu_list)

        elif user_msg == "로또":
            numbers = list(range(1,46)) 
            result = sorted(random.sample(numbers, 6))
        
        elif user_msg == "배달":
            phonebook = {
            "BBQ":"062-111-1111",
            "교촌":"062-222-2222",
            }
            choice = random.choice(list(phonebook.keys()))
            result = f"{choice} : {phonebook[choice]}"

        elif user_msg[0:2] == "번역":
            raw_text = user_msg[3:] 
            papago_url = "https://openapi.naver.com/v1/papago/n2mt"
            data = {
                "source":"ko",
                "target":"en",
                "text":raw_text
            }
            header = {
                'X-Naver-Client-Id':naver_id,
                'X-Naver-Client-Secret':naver_secret
            }
            
            res = requests.post(papago_url, data=data, headers=header)
            translate_res = res.json()
            translate_result = translate_res.get('message').get('result').get('translatedText')
            result = translate_result

        elif user_msg == "저녁 외식":
            menu_list = ['아빠가 쏜다!','아빠가 쏜다!','엄마가 쏜다!','딸이 쏜다!','아들이 쏜다!']
            result = f"오늘 저녁은 {random.choice(menu_list)}"

        elif user_msg[0:2] == "오늘":
            text = user_msg[3:] 
            who = ['엄마가','아빠가','엄마가','아빠가','딸이','아들이','아들이']
            clean = ['엄마가','아빠가','딸이','아들이']
            result = f"오늘 {text}은 {random.choice(who)} 만들고, 설거지는 {random.choice(clean)} 하자!"
        
        elif user_msg == "오늘 뭐먹지":
            menu_list = ['삼계탕', '철판낙지볶음', '물냉면','굶기']
            result = random.choice(menu_list)




        else:
            result = user_msg
    
    else:
        # 사용자가 보낸 사진을 찾는 과정
        result = "다운로드"
        file_id = data.get('message').get('photo')[-1].get('file_id')
        file_url = f"{api_url}/bot{token}/getFile?file_id={file_id}"
        file_res = requests.get(file_url)
        file_path = file_res.json().get('result').get('file_path')
        file = f"{api_url}/file/bot{token}/{file_path}"
        
       
        # 사용자가 보낸 사진을 클로버로 전송
        res = requests.get(file, stream=True)
        clova_url = "https://openapi.naver.com/v1/vision/celebrity"
        
        header = {
                'X-Naver-Client-Id':naver_id,
                'X-Naver-Client-Secret':naver_secret
            }
        clova_res = requests.post(clova_url, headers=header, files={'image':res.raw.read()})

        if clova_res.json().get('info').get('faceCount'):
            #누구랑 닮았는지 출력
            celebrity = clova_res.json().get('faces')[0].get('celebrity')
            print(celebrity)
            name = celebrity.get('value')
            confidence = celebrity.get('confidence')
            result = f"{name}일 확률이 {confidence*100}입니다."  
        else:
            # 사람이 없음
            result = "사람이 없습니다"
    


      




    res_url = f"{api_url}/bot{token}/sendMessage?chat_id={user_id}&text={result}"
    requests.get(res_url)


    return '', 200






if __name__=="__main__":
    app.run(debug=True)

