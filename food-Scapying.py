import requests
from bs4 import BeautifulSoup
import pandas as pd
link = "http://www.ipeen.com.tw/search/taipei/000/1-0-0-0/?baragain=1&so=sat"
NextPage = "http://www.ipeen.com.tw"
count = 1
alldata = []
tmplink = []
def SplitStr(InputStr):               #宣告副程式
        city = ""                     #用來存取區域的變數名稱宣告成string的型態
        citybool = False              #用來略過主要城市存取區域的布林
        for x in InputStr:
                if citybool == True:  #如果可以開始讀取區域的字串
                        city+=x
                if x=="縣"or x=="市": #已經讀到"市"或"縣" 就可以開始存區域的名稱
                       citybool = True
                if x=="區":           #讀到區的時候跳出
                        break;
        return city
def toIntger(inputNum):               #將list的型態變成字串 應該有更簡潔的方法
        tmp =""
        for x in inputNum:
                tmp +=x
        if tmp.isdigit():
                return int(tmp)
        else:
                return tmp
#================================================================
for x in range(1,int(input("請輸入要讀取得頁數 : "))+1):
        res = requests.get(link+"&p="+str(x))                   #用來翻頁
        soup = BeautifulSoup(res.text,"html.parser")            #用 BeautifulSoup 去接
        clean = soup.select(".serItem")
        for item in clean:
                shop = item.select('.a37.ga_tracking')[0].text.strip()
                tmp = filter(str.isdigit, item.select('.costEmpty')[0].text.strip().split()[1]) #使用filter函式取出數字
                price = toIntger(tmp) #將字串變成int型態
                tmp = filter(str.isdigit, item.select('.score')[0].text.strip())                #使用filter函式取出數字
                score = toIntger(tmp) #將字串變成int型態
                category = item.select('.cate')[0].text.strip().split("/")[0].split("\xa0")[0]
                address = item.select('.basic')[0].text.strip().split("：")[2].split("\t")[0].strip("\n")
                fulladdress = address
                address = SplitStr(address)
                if price != 0 and score!=0:
                        print('========[',count,']========')
                        alldata.append([shop,price,score,category,address,fulladdress]) #取出詳細資料的網址
                        tmplink.append(NextPage+item.find('a')['href'])
                        count += 1
print('========[第一次結束]========')
count=1
for x in range(len(tmplink)):                                                           #詳細資料的處理             
        print('========[',count,']========')
        soup = BeautifulSoup(requests.get(tmplink[x]).text,"html.parser")
        for item in soup.select(".scalar"):
                tmp = filter(str.isdigit,item.select('em')[1].text.strip())
                tmp = int(toIntger(tmp))
                alldata[x].append(tmp)
                break;
        count+=1
shop = [x[0] for x in alldata]
click = [x[6] for x in alldata]
score = [x[2] for x in alldata]
price = [x[1] for x in alldata]
address = [x[4] for x in alldata]
fulladdress=[x[5] for x in alldata]
category = [x[3] for x in alldata]
select = {'店名':shop,'區域名稱':address,'類型':category,'平均消費':price,'評論人數':score,'點擊次數':click,'地址':fulladdress}
cost_and_click=pd.DataFrame(select)
writer = pd.ExcelWriter('dataFood.xlsx')
cost_and_click.to_excel(writer,'愛評網')
writer.save()
