import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib

CE = ['http://sejong.ac.kr/college/software_01_1.html', 'http://abeek.sejong.ac.kr/abeek/program0302.html']
SW = ['http://sejong.ac.kr/college/software_03_1.html', 'http://abeek.sejong.ac.kr/abeek/program0502.html']
IS = ['http://sejong.ac.kr/college/software_02_1.html', 'http://abeek.sejong.ac.kr/abeek/program0602.html']
DS = ['http://sejong.ac.kr/college/software_04_1.html', 'http://abeek.sejong.ac.kr/abeek/program1602.html']
IE = ['http://sejong.ac.kr/college/software_05_1.html', 'http://abeek.sejong.ac.kr/abeek/program1702.html']
DI = ['http://sejong.ac.kr/college/software_06_1_1.html','http://home.sejong.ac.kr/~design/8.html']
CA = ['http://sejong.ac.kr/college/software_06_2_1.html','http://home.sejong.ac.kr/~anitec/18.html']

def info(dp):
  if dp == 'CE':
    target = CE[0]
  elif dp == 'SW':
    target = SW[0]
  elif dp == 'IS':
    target = IS[0]
  elif dp == 'DS':
    target = DS[0]
  elif dp == 'IE':
    target = IE[0]
  elif dp == 'DI':
    target = DI[0]
  elif dp == 'CA':
    target = CA[0]
  else:
    return False

  source = requests.get(target).text
  soup = BeautifulSoup(source, "html.parser")
  text = soup.select("div#content > div")[3]
  text = text.select('p')
  text = '\n'.join([ i.text for i in text ])
  
  return text


def graduation_condition(year):
  if len(year) != 4 or not year.isdigit():
    if len(year) != 2:
      return False

      
  if len(year) == 4:
    year = year[2:]

  result = [year+"-1.jpg", year+"-2.jpg"]
  if year == '13':
    del result[1]

  return result
 
 
def curriculum(dp):
  if dp == 'CE':
    target = CE[1]
  elif dp == 'SW':
    target = SW[1]
  elif dp == 'IS':
    target = IS[1]
  elif dp == 'DS':
    target = DS[1]
  elif dp == 'IE':
    target = IE[1]
  elif dp == 'DI':
    target = DI[1]
  elif dp == 'CA':
    target = CA[1]
  else:
    return False

  if (dp!='DI' and  dp!='CA'):
    source = requests.get(target).text
    soup = BeautifulSoup(source, "html.parser", from_encoding='utf-8')
    cururl=soup.select('a')[0]["href"]
    url='http://abeek.sejong.ac.kr/abeek/'+cururl
  else:
    url = target

  source2=requests.get(url)
  cur20= BeautifulSoup(source2.content.decode('euc-kr','replace'))
  if (dp=='DI'or dp=='CA'):
    imgurl=cur20.select("img")[1]["src"]
  else:
    imgurl=cur20.find("img")["src"]
    imgurl=urllib.parse.quote(imgurl)

  imgurl= url[:url.find('/', 7)]+imgurl
  urllib.request.urlretrieve(imgurl,"test.jpg")

  if (dp=='IE'):
    imgurl2=cur20.select("img")[1]["src"]
    imgurl2 = ''.join(imgurl2.split())
    imgurl2=urllib.parse.quote(imgurl2)
    imgurl2=url[:url.find('/', 7)]+imgurl2
    urllib.request.urlretrieve(imgurl2,"test2.jpg")
    return ["test.jpg","test2.jpg"]
  return ["test.jpg"]

def accreditation(dp):
  if (dp=='DI' or dp=='CA'):
    return False
  result = [dp+"_acc.png"]
  return result