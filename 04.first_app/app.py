from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "안녕하세요!!!"

@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하세요</h1>"

@app.route("/html_tags")
def html_tags():
    return """
    <h1>안녕하세요</h1>
    <h2>반갑습니다</h2>
    """
    
import datetime
@app.route("/dday")
def dday():
    today = datetime.datetime.now()
    endday = datetime.datetime(2019,11,29)
    d = endday-today
    return f"1학기 종료까지 {d.days}일 남음!!"

@app.route("/html_file")
def html_file():
    return render_template("index.html")

@app.route("/greeting/<string:name>")
def greeting(name):
    return f"안녕하세요 {name}님!!"

@app.route("/cube/<int:num>")
def cube(num):
    R = num **3
    return f"{num}의 세제곱은 {R}입니다."

@app.route("/cube_html/<int:num>")
def cube_html(num):
    cube_num = num**3
    return render_template("cube.html", num_html=num, cube_num_html=cube_num)

@app.route("/greeting_html/<string:name>")
def greeting_html(name):
    return render_template("greeting.html", name=name)

import random
@app.route("/lunch")
def lunch():
    menu = {
        "짜장면":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Jajangmyeon_by_stu_spivack.jpg/240px-Jajangmyeon_by_stu_spivack.jpg",
        "짬뽕":"http://recipe1.ezmember.co.kr/cache/recipe/2017/02/18/42ec50c7c281289367d1e7e4d06f4fcc1.jpg",
        "스파게티":"http://ko.sukpasta.wikidok.net/api/File/Real/578c682d5e1a20ee46f0264e"
    }

    menu_list = list(menu.keys()) #['짜장면'."짬뽕","스파게티"]
    pick = random.choice(menu_list)
    img = menu[pick]

    return render_template("lunch.html", pick=pick, img=img)

@app.route("/movies")
def movies():
    movie_list = ['스파이더맨','토이스토리','존윅3','알라딘']
    return render_template("movies.html", movie_list = movie_list)


@app.route("/ping")
def ping():
    return render_template("ping.html")

@app.route("/pong")
def pong():
    user_input = request.args.get("test")
    return render_template("pong.html", user_input= user_input)


@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")


@app.route('/text')
def text():
    return render_template("text.html")

import requests

@app.route('/result')
def result():
    raw_text = request.args.get("raw")
    url = "http://artii.herokuapp.com/make?text="
    res = requests.get(url+raw_text).text
    return render_template("result.html", res=res)


@app.route('/random_game')
def random_game():
    people = {
        "강호동":"https://file.mk.co.kr/meet/neds/2016/04/image_readtop_2016_307794_14618100732451425.jpg",
        "원빈":"https://i.pinimg.com/originals/1c/bd/ef/1cbdef0807e72f8cf1b0c26438676b44.png",
        "봉준호":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbjfNe7QVRiZ95zSH9TwU1yY8Lq0Gbime2y_gVboy3JfbRFNHehg",
        "수지":"http://www.topstarnews.net/news/photo/201905/629170_322988_2657.jpg",
        "신동엽":"http://mblogthumb2.phinf.naver.net/20150908_269/ssook410_1441714563692gVbQJ_JPEG/image.JPEG?type=w2",
        "조세호":"http://www.topstarnews.net/news/photo/201807/448382_99792_3244.jpg",
        "장도연":"https://cphoto.asiae.co.kr/listimglink/1/2017050318120314146_1.jpg",
    }

    people_list = list(people.keys()) #['강호동',"원빈","봉준호",'수지','신동엽','조세호','장도연']
    pick = random.choice(people_list)
    img = people[pick]

    return render_template("random_game.html", pick=pick, img=img)


@app.route("/pongpong")
def pongpong():
        user_input = request.args.get("test")
        return render_template("pongpong.html")






@app.route('/lotto')
def lotto():
    return render_template("lotto.html")

@app.route('/lotto_result')
def lotto_result():

    numbers = request.args.get("numbers").split()
    user_numbers = []
    for n in numbers:
        user_numbers.append(int(n))

    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=864"
    res = requests.get(url)
    lotto_numbers = res.json()
    
    winning_numbers = []
    for i in range(1,7):
        winning_numbers.append(lotto_numbers[f'drwtNo{i}'])
    bonus_number = lotto_numbers['bnusNo']


    result = "1등" 
    
    matched = len(set(user_numbers) & set(winning_numbers))
    if matched ==6:
        result = "1등"
    elif matched == 5:
        result = "3등"
    elif matched == 4:
        result = "4등"
    elif matched == 3:
        result = "5등"
    else:
        result = "꽝"


    return render_template("lotto_result.html", u=user_numbers, w=winning_numbers, b=bonus_number, r=result)












if __name__== '__main__':
    app.run(debug=True)