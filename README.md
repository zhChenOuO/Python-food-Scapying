# 美食網爬取資料分析

## 目的
1. 查看台北熱門美食的分布區域
2. 學習爬取網路上的資料
3. 學習 excel IO
4. 針對指定的html class物件做篩選

## 環境設置
```
> pip install BeautifulSoup
> pip install pandas
> pip install requests
> pip install matplotlib
> pip install xlrd
```
## 使用技術
1. Requests(GET)取得整張網頁內容
2. BeautifulSoup 查詢有 .serItem 的 內容
3. pandas 檔案的寫入
4. xlrd 檔案的讀入
5. Counter 計算該城市有多少排名上的美食
6. matplotlib 圓餅圖的繪製

##研究成果

![圓餅圖](https://github.com/OsbornOuO/Python-food-Scapying/blob/master/Figure_1.png)
![excel]()
1. 台北地區在美食網上的排名，第一是大安區、第二是中山區、第三是松山區
2. 