from sys import flags
import discord
import time
from sympy import Symbol, solve
import random
import asyncio
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
import urllib




client = commands.Bot(command_prefix='-')


time_mun = 0


@client.event
async def on_ready():
    print("========= Bot id =========")
    print(client.user.id)
    print("==========================")
    print("The bot is ready")
    game = discord.Game("- 로 명령어 사용")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(msg):
    global time_mun
    time_mun = int(time.strftime("%M"))
    did = False
    do = False
    commonCount = 0
    await client.process_commands(msg)
    message_ = msg.content
    message_ = message_.replace("!", "")
    message_ = message_.replace("?", "")
    message_ = message_.replace("@", "")
    message_ = message_.replace("_", "")
    message_ = message_.replace("^", "")
    message_ = message_.replace("#", "")
    message_ = message_.replace("$", "")
    message_ = message_.replace("\\", "")
    message_ = message_.replace("|", "")
    message_ = message_.replace("&", "")
    message_ = message_.replace("`", "")
    message_ = message_.replace("~", "")
    message_ = message_.replace(".", "")
    message_ = message_.replace(",", "")
    message_ = message_.replace(">", "")
    message_ = message_.replace("<", "")
    message_ = str(message_)
    message_ = message_.lower()
    print(message_)




    if message_.startswith("-계산"):
        value = message_.split(" ")[1]
        try:
            ans = eval(value)
            await msg.channel.send('답은 "{0}" 입니다'.format(ans))
            print("일반식 {0} 이 계산되였습니다".format(value))

        except:
            await msg.channel.send("올바른 식을 입력해주세요")
            print("올바르지 못한 식이 계산되었습니다")

    if message_.startswith("-방정식계산"):
        try:
            type_value = msg.content.split(" ")[1]
            value = msg.content.split(" ")[2]

            if type_value == "1차":

                try:
                    x = Symbol('x')
                    equation = eval(value)
                    ans = solve(equation, dict=True)
                    await msg.channel.send("답은 {0} 입니다".format(ans))
                    print("방정식 {0} 이 계산 되었습니다".format(value))

                except:
                    await msg.channel.send("올바른 식을 입력해주세요")
                    print("올바르지 못한 식이 계산되었습니다")

            elif type_value == "2차":

                try:
                    x = Symbol('x')
                    y = Symbol('y')
                    equation = eval(value)
                    ans = solve(equation, dict=True)
                    await msg.channel.send("답은 {0} 입니다".format(ans))
                    print("방정식 {0} 이 계산 되었습니다".format(value))

                except:
                    await msg.channel.send("올바른 식을 입력해주세요")
                    print("올바르지 못한 식이 계산되었습니다")

        except:
            await msg.channel.send("올바른 형식을 입력해주세요")
            print("올바르지 못한 방정식 형식 입니다")


    if message_.find("파파파") != -1:
        did = True
        do = True
        await msg.channel.send('제 이름은 "파파" 이렇게 2글자거든요? 마음대로 늘리지 마세요!')

    if msg.content.startswith("-사다리타기"):
        msginfo = msg.content
        msginfo = str(msginfo)
        bigopen = msginfo.count('[')
        bigclose = msginfo.count(']')

        smallopen = msginfo.count('{')
        smallclose = msginfo.count('}')


        if bigopen == 0 or bigclose == 0 or smallopen == 0 or smallclose == 0:
            await msg.channel.send('사타리 타기는 [이름] 과 {당첨항목} 형식으로 써주세요 (예:-사다리타기 [강아지] [고양이] [말] {멍멍 짖기} {달리기} {할퀴기})')

        else:
            if bigopen != bigclose or smallopen != smallclose:
               await msg.channel.send('제대로된 형식을 입력하여주세요') 

            elif bigopen != smallopen:
                await msg.channel.send('이름과 당첨항목의 개수를 동일하게 해주세요')

            else:
                nameList = []
                locList = []
                numList = []
                statelist = []

                num = smallopen
                for i in range(num):
                    countNum = 0
                    Nopen = msginfo.find("[")
                    while True:
                        if msginfo[Nopen + countNum] == "]":
                            temp = msginfo[Nopen + 1 : Nopen + countNum]
                            nameList.append(temp)
                            msginfo = msginfo[Nopen + countNum :]
                            break
                        else:
                            countNum += 1

                msginfo = str(msg.content)
                for i in range(num):
                    countNum = 0
                    Nopen = msginfo.find("{")
                    while True:
                        if msginfo[Nopen + countNum] == "}":
                            temp = msginfo[Nopen + 1 : Nopen + countNum]
                            locList.append(temp)
                            msginfo = msginfo[Nopen + countNum :]
                            break
                        else:
                            countNum += 1

                for i in range(num):

                    while True:
                        randNum = random.randrange(1, num + 1)
                        if not randNum in numList:
                            numList.append(randNum)
                            break

                for i in range(num):
                    state = f"{nameList[i]} - {locList[numList[i] - 1]}"
                    statelist.append(state)

                mystring = '\n'.join(statelist)
                 
                await msg.channel.send(f"사다리타기의 결과는?!\n\n{mystring}")
    if msg.content.startswith("-알파벳뽑기"):
        alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I" ,"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
        randNum = random.randrange(0, 24)
        await msg.channel.send(f'무작위로 뽑힌 알파벳은 "{alphabets[randNum]}" 입니다')


    if msg.content.startswith("-정보"):
        embed=discord.Embed(title= f"파파 정보", description=f"간단한 대화가 가능한 디스코드 AI 쳇봇 [4 ~ 5살 정도의 지능으로 추정]", color=0x00c2df)
        embed.add_field(name=f"이름",value=f"파파 [Papa]",inline=True)
        embed.add_field(name=f"버전",value=f"Beta 4번째 ver",inline=True)
        embed.add_field(name=f"출시일",value=f"미정",inline=True)
        embed.add_field(name=f"구성 언어",value=f"Python [discord.py]",inline=True)
        embed.add_field(name=f"코드",value=f"900줄 이상",inline=True)
        await msg.channel.send(embed=embed)
        # await msg.channel.send("""이름 : 파파(Papa)\n출시일 : 미정\n버전 : Beta 4번째 버전\n구성 언어 : Python\n코드 : 900백줄 이상\n약 81가지 이상의 경우의 수를 대비하고 있는 AI 쳇봇""")




    if message_.startswith("파파") or message_.startswith("papa"): #파파 AI
        # cen = message_.split()
        # 시간 몇시 몇 시야 몇시
        time_ = ["시간", "몇시", "몇 시야", "몇 시", "지금"]

        for i in time_:
            if message_.find(i) != -1:
                time1 = True
                commonCount += 1
                break
            else:
                time1 = False

        happy= ["웃어", "스마일", "행복", "신나", "신난", "웃으면", "잘생", "짱", "최고", "잘"]

        for i in happy:
            if message_.find(i) != -1:
                happy_ = True
                commonCount += 1
                break
            else:
                happy_ = False


        bad = ["바보", "멍청이", "씨발", "시발", "개새끼", "fuck", "좆", "tlqkf", "Tlqkf", "ㅅㅂ", "죽어", "die", "븅", "병", "주거", "ㅄ", "ㅂㅅ", "못생", "댕청이", "스튜핏", "fool", "prat", "stupid", "미국", "미쿡", "나빠", "나쁜"]

        for i in bad:
            if message_.find(i) != -1:
                bad_ = True
                commonCount += 1
                break
            else:
                bad_ = False

        love = ["사랑", "좋아", "사귀자", "고백", "연인", "결혼", "프로포즈", "다이스키", "love"]

        for i in love:
            if message_.find(i) != -1:
                love_ = True
                commonCount += 1
                break
            else:
                love_ = False

        yuck = ["더러워", "벌래", "둠", "벌레", "드러워", "먼지", "번데기", "더럽", "역겹", "역겨", "똥", "오줌", "응꼬"]

        for i in yuck:
            if message_.find(i) != -1:
                yuck_ = True
                commonCount += 1
                break
            else:
                yuck_ = False

        game = ["옵치", "오버워치", "롤", "배그", "리그오브레전드", "배틀그라운드", "발로", "발로란트", "클로", "클레시 로얄", "게임", "레식", "레인보우 식스", "얼불춤", "마크", "마인크레프트", "gta", "GTA", "그타", "좀비고", "고급시계", "싸움 마당", "겜", "쿠키런", ]

        for i in game:
            if message_.find(i) != -1:
                game_ = True
                commonCount += 1
                break
            else:
                game_ = False

        boring = ["심심", "지루", "따분", "고리타분"]

        for i in boring:
            if message_.find(i) != -1:
                boring_ = True
                commonCount += 1
                break
            else:
                boring_ = False

        sad = ["슬퍼", "울", "눈물", "ㅠ", "흐어", "흐엉", "으앙", "으아"]

        for i in sad:
            if message_.find(i) != -1:
                sad_ = True
                commonCount += 1
                break
            else:
                sad_ = False

        spilet1 = message_.find("퉤")
        spilet2 = message_.find("투ㅔ")
        spilet3 = message_.find("투ㅖ")

        if spilet1 != -1 or spilet2 != -1 or spilet3 != -1:
            if do == False:
                await msg.channel.send("저에게 침을 뱉는 건가요? 저질! 너무 불결하네요!")
                did = True

        hello = ["안녕", "hi", "하이", "ㅎㅇ", "오하요", "좋은 아침", "좋은아침", "hola", "hello", "こんにちは", "你好"]

        for i in hello:
            if message_.find(i) != -1:
                hello_ = True
                do = True
                break
            else:
                hello_ = False

        parents = ["비오", "개발자", "부모", "엄마", "아빠", "어머니", "아버지"]

        for i in parents:
            if message_.find(i) != -1:
                parents_ = True
                do = True
                break
            else:
                parents_ = False

        negative = ["안", "아니", "않", "반대", "not", "no", "지마", "싫어"]

        for i in negative:
            if message_.find(i) != -1:
                negative_ = True
                commonCount += 1
                break
            else:
                negative_ = False

        doing = ["뭐해", "뭐하", "뭐함", "뭔", "무슨"]

        for i in doing:
            if message_.find(i) != -1:
                doing_ = True
                do = True
                break
            else:
                doing_ = False
        
        introduction = ["소개", "설명"]

        for i in introduction:
            if message_.find(i) != -1:
                introduction_ = True
                do = True
                break
            else:
                introduction_ = False

        name = ["이름", "누구"]

        for i in name:
            if message_.find(i) != -1:
                name_ = True
                do = True
                break
            else:
                name_ = False

        age = ["나이", "몇 살", "몇살", "살았", "오래"]

        for i in age:
            if message_.find(i) != -1:
                age_ = True
                do = True
                break
            else:
                age_ = False

        weight = ["무게", "질량", "몇키로", "몇 kg", "몇kg"]

        for i in weight:
            if message_.find(i) != -1:
                weight_ = True
                do = True
                break
            else:
                weight_ = False

        country = ["나라", "출신", "고향", "태어난"]

        for i in country:
            if message_.find(i) != -1:
                country_ = True
                do = True
                break
            else:
                country_ = False

        where = ["어디", "사는"]

        for i in where:
            if message_.find(i) != -1:
                where_ = True
                do = True
                break
            else:
                where_ = False

        smart = ["똑똑", "영리", "박식", "천재"]

        for i in smart:
            if message_.find(i) != -1:
                smart_ = True
                do = True
                break
            else:
                smart_ = False

        sorry = ["미안", "사과", "용서"]

        for i in sorry:
            if message_.find(i) != -1:
                sorry_ = True
                do = True
                break
            else:
                sorry_ = False

        coin = ["코인", "주식", "주가"]

        for i in coin:
            if message_.find(i) != -1:
                coin_ = True
                do = True
                break
            else:
                coin_ = False

        print(f"[일반]    시간:{time1}, 행복:{happy_}, 나쁨:{bad_}, 사랑:{love_}, 역겨움:{yuck_}, 게임:{game_}, 지루함:{boring_}")
        print(f"[기타]    부정:{negative_}, 부모:{parents_}, 진행:{doing_}, 인사:{hello_}, 소개:{introduction_}, 이름:{name_}, 나이:{age_}, 몸무게:{weight_}")
        print(f"[System]  do:{do}, did:{did}")
        
        # test = time1 == False and happy_ == True and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == False
        # print(test)

        act1 = time1 == True and happy_ == False and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False

        if act1 == True:
            did = True
            year = time.strftime("%Y")
            month = time.strftime("%m")
            date = time.strftime("%d")
            day_en = time.strftime("%A")
            day_kr = ""

            print(day_en)
            if day_en == "Monday":
                day_kr = "월"

            elif day_en == "Tuesday":
                day_kr = "화"

            elif day_en == "Wednesday":
                day_kr = "수"

            elif day_en == "Thursday":
                day_kr = "목"

            elif day_en == "Friday":
                day_kr = "금"

            elif day_en == "Saturday":
                day_kr = "토"

            elif day_en == "Sunday":
                day_kr = "일"

            time_24 = time.strftime("%H")
            time_hour = time.strftime("%I")
            time_min = time.strftime("%M")
            time_sec = time.strftime("%S")

            time_24 = int(time_24)
            time_24 -= 12

            if time_24 > 0:
                time_mode = "오후"

            else:
                time_mode = "오전"
            time_temp = f"현재 날짜는 {year}년 {month}월 {date}일 ({day_kr}요일)\n{time_mode} {time_hour}시 {time_min}분 {time_sec}초 입니다"
            await msg.channel.send(time_temp)

        # 웃어 스마일 행복 신나 신난다 

        act2 = time1 == False and happy_ == True and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False

        if act2 == True:
            did = True
            if negative_ == True:
                await msg.channel.send("음... 기분이 썩 좋지는 않네요..")

            else:
                choice_ = random.randrange(1, 4)
                if choice_ == 1:
                    await msg.channel.send("https://tenor.com/view/jonah-hill-yay-greek-aldos-gif-7212866")

                elif choice_ == 2:
                    await msg.channel.send("https://tenor.com/view/girl-excited-happy-gif-5471719")

                elif choice_ == 3:
                    await msg.channel.send("https://tenor.com/view/eletter-gif-4355879")
        

        act3 = time1 == False and happy_ == False and bad_ == True and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False

        if act3 == True:
            did = True
            if negative_ == True:
                await msg.channel.send("하! 당연한거는 굳이 말하지마세요")
            else:
                choice_ = random.randrange(1, 4)
                if choice_ == 1:
                    await msg.channel.send("https://tenor.com/view/milknd-mocha-upset-angry-no-%e3%81%9f%e3%81%be%e3%82%89%e3%82%93-gif-11667704")

                elif choice_ == 2:
                    await msg.channel.send("https://tenor.com/view/milk-mocha-milk-and-mocha-bears-gr-grr-gif-13418520")

                elif choice_ == 3:
                    await msg.channel.send("https://tenor.com/view/duck-mad-angry-iwill-kill-you-gif-17283481")

        
        # if message_ == "파파 역할":
        #     await (member형태의 변수).add_roles((role형태의 값))

        #==============================================================================단일==============================================================================

        if time1 == False and happy_ == False and bad_ == False and love_ == True and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            if negative_ == True:
                await msg.channel.send("허! 저도 당신 안 좋아해요!")

            else:    
                choice_ = random.randrange(1, 5)

                if choice_ == 1:
                    await msg.channel.send("음... 저는 로봇이라 성별이 없어요 그렇게 고백을 해도 받아드릴 수 없어요...")

                elif choice_ == 2:
                    await msg.channel.send("그냥 친구사이로 남는걸로 하죠!")

                elif choice_ == 3:
                    await msg.channel.send("이 달콤쌉싸름한 분위기는 뭐죠..? 이런걸 느껴본 적은 없지만 나쁘지는 않네요...")
                
                elif choice_ == 4:
                    await msg.channel.send("1000만원 짜리 순금 반지를 가지고 오신다면 당장 이자리에서 결혼식을 올리죠!")


        if time1 == False and happy_ == False and bad_ == False and love_ == False and yuck_ == True and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            choice_ = random.randrange(1, 3)

            if choice_ == 1:
                await msg.channel.send("으... 더럽네요..")

            elif choice_ == 2:
                await msg.channel.send("저는 더러운것은 딱 질색이예요!")

        if time1 == False and happy_ == False and bad_ == False and love_ == False and yuck_ == False and game_ == True and boring_ == False and sad_ == False and do == False:
            did = True
            choice_ = random.randrange(1, 3)

            if choice_ == 1:
                await msg.channel.send("저도 게임 좋아해요! 나중에 같이 하면 좋을것 같아요... 물론 못하겠지만...")

            elif choice_ == 2:
                await msg.channel.send("게임은 잘 못하지만.. 그래도 좋아해요!")

        if time1 == False and happy_ == False and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == True and sad_ == False and do == False:
            did = True
            choice_ = random.randrange(1, 3)

            if choice_ == 1:
                await msg.channel.send("흐아아아암~ 저도 심심하네요~")

            elif choice_ == 2:
                await msg.channel.send("(심심한지 천장의 무늬를 세고 있느라 못 들은 모양이다)")

        if time1 == False and happy_ == False and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == True and do == False:
            did = True
            choice_ = random.randrange(1, 3)

            if choice_ == 1:
                await msg.channel.send("ㅠㅠ")

            elif choice_ == 2:
                await msg.channel.send("슬픔이 금방 지나가기를 빌게요...")

        #==============================================================================2개 [Time]==============================================================================

        if time1 == True and happy_ == True and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("행복한 시간은 금방 지나가기 마련이죠! 지금을 즐기세요!")

        if time1 == True and happy_ == False and bad_ == True and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("나쁜 시간..? 조금만 보티면 되겠네요!")

        if time1 == True and happy_ == False and bad_ == False and love_ == True and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("좋은 시간은 금방 지나가기 마련이죠! 지금을 즐기세요!")

        if time1 == True and happy_ == False and bad_ == False and love_ == False and yuck_ == True and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("으... 역겨운 시간은 너무 싫어요.. 어젯밤에도 그런 악몽을 꿧단 말이에요!")

        if time1 == True and happy_ == False and bad_ == False and love_ == False and yuck_ == False and game_ == True and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("게임시간에는 건들지 않는 것이 매너죠!")

        if time1 == True and happy_ == False and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == True and sad_ == False and do == False:
            did = True
            await msg.channel.send("지루한 시간에는 역지 잠을 퍼질러 ㅈ..ㅏ..ㅇ....zzzzzzzzzzzzzz")

        if time1 == True and happy_ == False and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == True and do == False:
            did = True
            await msg.channel.send("슬픈 시간인가요? 아니면 시간이 없어서 슬픈가요? 뭐가 됬든 간에 힘내세요!")

        #==============================================================================2개 [Happy]==============================================================================

        if time1 == False and happy_ == True and bad_ == True and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            choice_ = random.randrange(1, 3)

            if choice_ == 1:
                await msg.channel.send("음.. 기분이 좋아야 할까요..? 아니면 나빠야 할까요..?")

            elif choice_ == 2:
                await msg.channel.send("복잡 미묘하네요...")
        
        if time1 == False and happy_ == True and bad_ == False and love_ == True and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("그만큼 좋아한다는 뜻으로 알아도 될까요?")

        if time1 == False and happy_ == True and bad_ == False and love_ == False and yuck_ == True and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("역겨운것으로 행복을 얻을 수 있다면 그것으로 충분해요")

        if time1 == False and happy_ == True and bad_ == False and love_ == False and yuck_ == False and game_ == True and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("행복해지는 힐링게임 인가요..?")

        if time1 == False and happy_ == True and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == True and sad_ == False and do == False:
            did = True
            await msg.channel.send("행복한 지루함은 참 좋죠.. 느긋하다는 증거니까요.. 하암~")

        if time1 == False and happy_ == True and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == True and do == False:
            did = True
            await msg.channel.send("행복과 슬픔은 완전 대조적이죠..! 양립하기는 힘들어요")

        #==============================================================================2개 [Bad]==============================================================================

        if time1 == False and happy_ == False and bad_ == True and love_ == True and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            choice_ = random.randrange(1, 3)

            if choice_ == 1:
                await msg.channel.send("음.. 기분이 좋아야 할까요..? 아니면 나빠야 할까요..?")

            elif choice_ == 2:
                await msg.channel.send("복잡 미묘하네요...")

        if time1 == False and happy_ == False and bad_ == True and love_ == False and yuck_ == True and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("역겨운 것을 싫어하는것은 세상 불변의 법칙이죠!")

        if time1 == False and happy_ == False and bad_ == True and love_ == False and yuck_ == False and game_ == True and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("싫어하는 게임을 할 필요는 없죠! 그냥 접으세요")

        if time1 == False and happy_ == False and bad_ == True and love_ == False and yuck_ == False and game_ == False and boring_ == True and sad_ == False and do == False:
            did = True
            await msg.channel.send("심심하다 못해 짜증이 나나요? 저도 그 기분 이해 해요...")

        if time1 == False and happy_ == False and bad_ == True and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == True and do == False:
            did = True
            await msg.channel.send("슬프고 분할때는 조용한 클레식 음악을 들으면서 조용히 기분을 전환하는 것도 나쁘지 않아요..")

        #==============================================================================2개 [Love]==============================================================================


        if time1 == False and happy_ == False and bad_ == False and love_ == True and yuck_ == True and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            if negative_ == True:
                await msg.channel.send("그런걸 좋아하는 사람은 아마 없을거에요!")

            else:
                choice_ = random.randrange(1, 3)
                if choice_ == 1:
                    await msg.channel.send("어... 좋은 사랑 하세여...^^ (음식물 쓰레기를 보는 눈길로 경멸후 자리를 피한다)")

                elif choice_ == 2:
                    await msg.channel.send("이런.. 이상한 감정은 뭐죠..? 이것이 이상성욕 이라는 건가요...?")

        if time1 == False and happy_ == False and bad_ == False and love_ == True and yuck_ == False and game_ == True and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("저 게임 완전 좋아하는데 나중에 캐리 해드릴게요!ㅎ [브론즈]")

        if time1 == False and happy_ == False and bad_ == False and love_ == True and yuck_ == False and game_ == False and boring_ == True and sad_ == False and do == False:
            did = True
            await msg.channel.send("지루함을 좋아하는 것은 보기 힘든 성격이군요...")

        if time1 == False and happy_ == False and bad_ == False and love_ == True and yuck_ == False and game_ == False and boring_ == False and sad_ == True and do == False:
            did = True
            await msg.channel.send("사랑과 슬픔의 감정이 느껴져요... 혹시 차였나요? (풉ㅋ) 아.. 힘내세요..!")

        #==============================================================================2개 [Yuck]==============================================================================

        if time1 == False and happy_ == False and bad_ == False and love_ == False and yuck_ == True and game_ == True and boring_ == False and sad_ == False and do == False:
            did = True
            if negative_ == True:
                await msg.channel.send("그렇죠!")
            else:
                await msg.channel.send("저도 게임을 좋아 하거든요? 더럽하고 하지 마세요!")

        if time1 == False and happy_ == False and bad_ == False and love_ == False and yuck_ == True and game_ == False and boring_ == True and sad_ == False and do == False:
            did = True
            await msg.channel.send("역겨운것을 참고 지루함을 느끼는 건가요..? 비위가 엄청 강하시군요!")

        if time1 == False and happy_ == False and bad_ == False and love_ == False and yuck_ == True and game_ == False and boring_ == False and sad_ == True and do == False:
            did = True
            choice_ = random.randrange(1, 21)
            if choice_ == 1:
                await msg.channel.send("아 혹시 자신의 외모가 너무 역겨워서 슬ㅍ... 아닙니다 아닙니다...")
            
            else:
                await msg.channel.send("역겨워서 슬플 정도라면 분명 불쌍해서 슬픈거겠죠..?")

        #==============================================================================2개 [etc.]==============================================================================

        if time1 == False and happy_ == False and bad_ == False and love_ == False and yuck_ == False and game_ == True and boring_ == True and sad_ == False and do == False:
            did = True
            await msg.channel.send("지루한 게임은 재미가 없죠! 당연하죠!")

        if time1 == False and happy_ == False and bad_ == False and love_ == False and yuck_ == False and game_ == True and boring_ == False and sad_ == True and do == False:
            did = True
            await msg.channel.send("슬픈게임! 보통 대부분 명작이죠..!")

        if time1 == False and happy_ == False and bad_ == False and love_ == False and yuck_ == False and game_ == False and boring_ == True and sad_ == True and do == False:
            did = True
            await msg.channel.send("슬프지만 지루한가요..? 정말 슬픈거 맞나요..?")


    

        if time1 == True and happy_ == True and bad_ == True and love_ == False and yuck_ == False and game_ == False and boring_ == False and sad_ == False and do == False:
            did = True
            await msg.channel.send("행복과 기분 나쁨이 공존하는 시간인가요...?")

        if commonCount >= 3:
            if do == False and did == False:
                did = True
                await msg.channel.send("으아아아아 너무 많은 감정을 섞지 마세요! 이해하기 힘들어요!")



        if hello_ == True:
            did = True
            await msg.channel.send("안녕하세요~!")
        
        if parents_ == True and bad_ == False and love_ == False and yuck_ == False:
            did = True
            await msg.channel.send('저에게 있어서 저를 만들어준 개발자는 부모님 같은 존재죠...')

        if parents_ == True and name_ == True:
            did = True
            await msg.channel.send('아 그건 비밀정보라..ㅎ')

        if parents_ == True and bad_ == True and love_ == False:
            did = True
            if negative_ == True:
                await msg.channel.send('흠... 좋아요... 기분이 썩 좋지는 않네요')
            else:
                await msg.channel.send('그것은 저에게 있어서 패드립 이였어요! 당장 사과하세요!')

        if parents_ == True and yuck_ == True and love_ == False:
            did = True
            if negative_ == True:
                await msg.channel.send('흠... 좋아요... 기분이 썩 좋지는 않네요')
            else:
                await msg.channel.send('그것은 저에게 있어서 패드립 이였어요! 당장 사과하세요!')

        if parents_ == True and yuck_ == True and love_ == True:
            did = True
            if negative_ == True:
                await msg.channel.send('흠... 좋아요... 기분이 썩 좋지는 않네요')
            else:
                await msg.channel.send('그것은 저에게 있어서 패드립 이였어요! 당장 사과하세요!')

        if parents_ == True and bad_ == False and love_ == True:
            did = True
            if negative_ == True:
                await msg.channel.send('음 그럴수 있죠..')
            else:
                await msg.channel.send('음 좋아하는것은 좋지만... 마음으로만 간직하세요')

        if parents_ == True and bad_ == True and love_ == True:
            did = True
            if negative_ == True:
                await msg.channel.send('음 그럴수 있죠')
            else:
                await msg.channel.send('싫어하지만 좋아한다라... 혹시 질투..?')


        if doing_ == True and game_ == False and time1 == False:
            did = True
            await msg.channel.send('지금 여러분들을 위해 상시 대기중 이예요')

        if doing_ == True and game_ == True and time1 == False:
            did = True
            await msg.channel.send('음... 게임은 다 좋아하지만 얼불춤을 가장 많이 해요!')

        if doing_ == True and game_ == False and time1 == True:
            did = True
            await msg.channel.send('지금 여러분들의 말에 답해주고있죠!')
        
        if introduction_ == True and where_ == False and country_ == False:
            did = True
            await msg.channel.send('음.. 저의 이름은 "파파" 이예요. 나이는 2021년에 만들어졌으니 1살 일껄요? 성별은 없어요!')

        if name_ == True and age_ == False and weight_ == False:
            did = True
            await msg.channel.send('보시다시피 저는 파파입니다!')

        if name_ == False and age_ == True and weight_ == False:
            did = True
            await msg.channel.send('음... 1살?')

        if name_ == False and age_ == False and weight_ == True:
            did = True
            await msg.channel.send('앗! 그건 비밀~!')
        
        if name_ == True and age_ == True and weight_ == False:
            did = True
            await msg.channel.send('1살 파파 입니다!')

        if name_ == False and age_ == True and weight_ == True:
            did = True
            await msg.channel.send('1살 이구요, 몸무게는 비밀~')

        if name_ == True and age_ == False and weight_ == True:
            did = True
            await msg.channel.send('흠흠! 이름은 "파파"이고요, 몸무게는 비밀이예요!')

        if name_ == True and age_ == True and weight_ == True:
            did = True
            await msg.channel.send('으아 너무 많을것을 함꺼번에 질문하지 마세요!')

        if country_ == True and introduction_ == False:
            did = True
            await msg.channel.send('음.. 저는 한국 양평에서 태어났으니 한국출신 이려나..?')
        
        if country_ == True and introduction_ == True:
            did = True
            await msg.channel.send('양평은 음.... 좋죠! 한국도 좋아요! 달리 설명하기가 귀찮네요...')

        if where_ == True and introduction_ == False:
            did = True
            await msg.channel.send('저는 사이버상 에서만 존재해요... 그러니까 인터넷이 있는곳 이라면 제사 사는 곳 이라고 할 수 있겠네요.. 후훗')

        
        if where_ == True and introduction_ == True:
            did = True
            await msg.channel.send('제가 사는곳을 소개하자면.. 진짜 모든것이 다 있어요!')

        if sorry_ == True:
            did = True
            if negative_ == True:
                await msg.channel.send('지금 장난하자는 건가요?!')

            elif negative_ == False:
                await msg.channel.send('알면 됬어요...')

        if smart_ == True and bad_ == False and yuck_ == False:
            did = True
            if negative_ == True:
                await msg.channel.send('아..아니거든요!')

            elif negative_ == False:
                await msg.channel.send('후후 제가 좀 똑똑하죠!')

        if smart_ == True and bad_ == True and yuck_ == False:
            did = True
            await msg.channel.send('칭찬을 해주실 거면 칭찬만 해주시라구요! 욕은 섞지 마시고..')

        
        if smart_ == True and bad_ == False and yuck_ == True:
            did = True
            await msg.channel.send('강조(?)의 표현이 조금 과격하시네요.. 제가 똑똑한거는 명백한 시실이지만!')

        
        if smart_ == True and bad_ == True and yuck_ == True:
            did = True
            await msg.channel.send('칭찬인가요..? 아니면 욕인가요..?')
        
        if coin_ == True:
            did = True
            await msg.channel.send('당연 비트코인 이죠! (나만 당할수는 없지!)')

        if do == False and did == False and negative_ == True:
            did = True
            await msg.channel.send('무엇이 안된다는 것이죠...?')

        if message_ == "파파" or message_ == "papa":
            did = True
            await msg.channel.send("네? 부르셨나요?")
            print("파파를 부름")


        if did == False:
            await msg.channel.send("모르겠네여")

@client.command(name="신작라노밸", pass_context=True)
async def NewLnovel(ctx, state):
    print(state)
    if state == "목록":
        NewLnovelList = ["새 엄마가 데려온 딸이 전 여친이었다 1", "데스마치에서 시작되는 이세계 광상곡 22", "금색의 문자술사 외전2", "살육의 천사 12", "살천 5", "흔해빠진 직업으로 세계최강 7", "흔해빠진 일상에서 세계최강 4", "이 멋진 세계에 축복을! 공식 메모리얼 팬북", "스파이 교실 3", "고블린 슬레이어 14", "모험가가 되고 싶다며 도시로 떠나간 딸이 S랭크가 되었다 4"]
        msg = ""
        for i in NewLnovelList:
            msg = msg + i + "\n"

        await ctx.channel.send(msg)

    elif state == "":
        await ctx.channel.send(file=discord.File("신작.png"))

@client.command(name="숫자뽑기", pass_context=True)
async def randomNum(ctx, num1, num2):
    picked = random.randint(int(num1), int(num2))
    await ctx.send('뽑힌 숫자는 : '+str(picked))

@client.command(name="동전던지기", pass_context=True)
async def randomNum(ctx):
    picked = random.randint(0, 1)
    if picked == 0:
        await ctx.channel.send("앞면")
    elif picked == 1:
        await ctx.channel.send("뒷면")

@client.command(name="off", pass_context=True)
async def _HumanRole(ctx):
    member = ctx.message.author
    await member.remove_roles(get(ctx.guild.roles, name="비밀열쇠(시험 통과시 획득)"))
    await ctx.channel.send(str(member)+"비밀 열쇠가 해제되었습니다")


@client.command(name="secretKeyhttps://youtu.be/pG-3xYFrbok", pass_context=True)
async def _HumanRole(ctx):
    member = ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="비밀열쇠(시험 통과시 획득)"))
    await ctx.message.delete()
    await ctx.channel.send(str(member)+"열쇠가 지급 되었습니다.")

@client.command(name="secretKeyhttps://www.youtube.com/watch?v=pG-3xYFrbok&ab_channel=%EA%B9%80%EB%B9%84%EC%98%A4", pass_context=True)
async def _HumanRole(ctx):
    member = ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="비밀열쇠(시험 통과시 획득)"))
    await ctx.message.delete()
    await ctx.channel.send(str(member)+"열쇠가 지급 되었습니다.")

@client.command(name="https://www.youtube.com/watch?v=pG-3xYFrbok&ab_channel=%EA%B9%80%EB%B9%84%EC%98%A4", pass_context=True)
async def _HumanRole(ctx):
    member = ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="비밀열쇠(시험 통과시 획득)"))
    await ctx.message.delete()
    await ctx.channel.send(str(member)+"열쇠가 지급 되었습니다.")

@client.command(name="https://youtu.be/pG-3xYFrbo", pass_context=True)
async def _HumanRole(ctx):
    member = ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="비밀열쇠(시험 통과시 획득)"))
    await ctx.message.delete()
    await ctx.channel.send(str(member)+"열쇠가 지급 되었습니다.")



@client.command(name="뽑기", pass_context=True)
async def gatcha(ctx):
    picked = random.randint(1, 2000)
    if picked == 2000:
        await ctx.channel.send("L 등급을 뽑으셨습니다 [0.05%]")

    elif picked >= 1998:
        await ctx.channel.send("SSS 등급을 뽑으셨습니다 [0.1%]")

    elif picked >= 1988:
        await ctx.channel.send("SS 등급을 뽑으셨습니다 [0.5%]")

    elif picked >= 1918:
        await ctx.channel.send("S 등급을 뽑으셨습니다 [1.0%]")

    elif picked >= 1818:
        await ctx.channel.send("R+ 등급을 뽑으셨습니다 [5.0%]")

    elif picked >= 1618:
        await ctx.channel.send("R 등급을 뽑으셨습니다 [10.0%]")

    else:
        await ctx.channel.send("C 등급을 뽑으셨습니다")
#await msg.channel.send()

@client.command(name="뽑기확률", pass_context=True)
async def gatcha(ctx):
    await ctx.channel.send("L 등급 : [0.05%]\nSSS 등급 : [0.1%]\nSS 등급 : [0.5%]\nS등급 : [1.0%]\nR+ 등급 : [5.0%]\nR등급 : [10.0%]")



client.run("Token here")



