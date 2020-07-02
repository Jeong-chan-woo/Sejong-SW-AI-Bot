import requests
import os
import json
import telegram
import time
from bs4 import BeautifulSoup
import urllib.request
import urllib
import crawling

#SW학과정보
DS = ['데이터사이언스학과', '데이터사이언스', '데이터싸이언스학과', '데이터싸이언스', '데싸', '데사', 'datascience', 'DataScience']
IE = ['지능기전공학부', '지기전', '지기']
CE = ['컴퓨터공학과', '컴퓨터 공학과', '컴공', '컴공과', '컴퓨터공학', '컴퓨터 공학']
SW = ['소프트웨어학과', '소웨과', '소웨', '소프트과', '소프트']
IS = ['정보보호학과', '정보 보호학과', '정보보호', '정보', '정보 보호']
DI = ['디자인이노베이션학과', '디자인이노베이션', '디이노', '디자이노베이션', '디노']
CA = ['만화애니메이션텍', '만화애니메이션텍학과', '만화애니메이션', '만화애니매이션학과', '만화애니매이션', '만애텍', '만에텍', '만애택', '만에택']

MAJOR = [DS, IE, CE, SW, IS, DI, CA]

#메뉴찾기
def find_menu(chat_message, major):
    if ("교과과정" in chat_message)==True or ("교과 과정" in chat_message)==True or ("교육과정" in chat_message)==True or ("교육 과정" in chat_message)==True:
        photo = crawling.curriculum(major)
        for i in photo:
            url_img = "https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendPhoto";
            files = {'photo': open(i, 'rb')}
            data = {'chat_id' : chat_id}
            r= requests.post(url_img, files=files, data=data)
        return True
    elif ("학사일정" in chat_message)==True or ("학사 일정" in chat_message)==True or ("일정" in chat_message)==True:
        url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendMessage'.format(token)
        requests.get(url, params = {"chat_id" : chat_id, "text" : '몇 월의 학사일정을 알고싶은가요?'})
        time.sleep(5)
        url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/getUpdates'.format(token)
        response = json.loads(requests.get(url).text)
        month = response["result"][-1]["message"]["text"]
        data = crawling.calendar(month)
        url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendMessage'.format(token)
        requests.get(url, params = {"chat_id" : chat_id, "text" : data})
        return True

    elif ("졸업요건" in chat_message)==True or ("졸업 요건" in chat_message)==True or ("졸업" in chat_message)==True:
        url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendMessage'.format(token)
        requests.get(url, params = {"chat_id" : chat_id, "text" : '입학연도를 알려주세요!'})
        time.sleep(5)
        url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/getUpdates'.format(token)
        response = json.loads(requests.get(url).text)
        year = response["result"][-1]["message"]["text"]
        photo = crawling.graduation_condition(year)
        for i in photo:
            url_img = "https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendPhoto";
            files = {'photo': open('졸업요건/'+i, 'rb')}
            data = {'chat_id' : chat_id}
            r= requests.post(url_img, files=files, data=data)
        return True
    elif ("공학인증" in chat_message)==True or ("공학 인증" in chat_message)==True or ("공학" in chat_message)==True:
        EA = crawling.accreditation(major)
        if EA != False:
            url_img = "https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendPhoto";
            files = {'photo': open("공학인증/"+EA[0], 'rb')}
            data = {'chat_id' : chat_id}
            r= requests.post(url_img, files=files, data=data)
        else:
            url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendMessage'.format(token)
            requests.get(url, params = {"chat_id" : chat_id, "text" : "해당 학과는 공학인증제도가 존재하지 않아요ㅠㅠ"})
        return True

    elif ("학과소개" in chat_message)==True or ("학과 소개" in chat_message)==True:
        a = crawling.info(major)
        url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendMessage'.format(token)
        requests.get(url, params = {"chat_id" : chat_id, "text" : a})
        return True
    else:
        return False

#학과 찾기
def find_major(chat_message):
    count=0
    for i in MAJOR:
        count+=1
        for j in i:
            if (j in chat_message)==True:
                if count==1:
                    return 'DS'
                elif count==2:
                    return 'IE'
                elif count==3:
                    return 'CE'
                elif count==4:
                    return 'SW'
                elif count==5:
                    return 'IS'
                elif count==6:
                    return 'DI'
                elif count==7:
                    return 'CA'
                else:
                    return
    return 'No'

#과사 전화번호
def major_number(major):
  if major=='DS':
    return "02-6935-2544"
  elif major=='IE':
    return "02-3408-3900"
  elif major=='CE':
    return "02-3408-3321"
  elif major=='SW':
    return "02-3408-3667"
  elif major=='IS':
    return "02-3408-4181"
  elif major=='DI':
    return "02-3408-3323"
  elif major=='CA':
    return "02-3408-3328"

#main
token = os.getenv('TELEGRAM_TOKEN')
url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/getUpdates'.format(token)
response = json.loads(requests.get(url).text)
print(response)
chat_id = response["result"][-1]["message"]["from"]["id"]
chat_message = response["result"][-1]["message"]["text"]

major = find_major(chat_message)

if major == 'No':
    url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendMessage'.format(token)
    requests.get(url, params = {"chat_id" : chat_id, "text" : '학과를 입력해주세요!'})
    time.sleep(5)
    url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/getUpdates'.format(token)
    response = json.loads(requests.get(url).text)
    chat_message = response["result"][-1]["message"]["text"]
    major = find_major(chat_message)

    if major == 'No':
        url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendMessage'.format(token)
        requests.get(url, params = {"chat_id" : chat_id, "text" : "세종대학교 소프트웨어융합대학에는 '데이터사이언스학과', '지능기전공학부', '컴퓨터공학과', '소프트웨어학과', '정보보호학과', '디자인이노베이션학과', '만화애니매이션텍학과'가 있어요.\n 원하시는 학과가 있다면 선택해주세요:) 없다면 죄송해요ㅠㅠ"})

#find_menu(chat_message, major)

if find_menu(chat_message, major) == False:
    url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendMessage'.format(token)
    requests.get(url, params = {"chat_id" : chat_id, "text" : '저에게 궁금한게 뭔가요?'})
    time.sleep(5)
    url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/getUpdates'.format(token)
    response = json.loads(requests.get(url).text)
    chat_message = response["result"][-1]["message"]["text"]
    menu = find_menu(chat_message, major)

    if menu == False:
        phonenumber = major_number(major)
        url = 'https://api.telegram.org/bot1313642468:AAEXuBga6sg5oiHvP3GWgz6xH3coJghL8T4/sendMessage'.format(token)
        requests.get(url, params = {"chat_id" : chat_id, "text" : '저는 잘 모르겠어요ㅜㅜ\n'+'학과 사무실 번호를 알려드릴게요!\n' + phonenumber+' 이 번호로 전화해주세요:)'})