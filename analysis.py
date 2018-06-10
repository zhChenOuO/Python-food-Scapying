import xlrd
from collections import Counter
from matplotlib import pyplot as plt


colors = ["red","coral","green","yellow","orange","purple","Indigo"]
data = xlrd.open_workbook('dataFood.xlsx')
table = data.sheet_by_name(u'愛評網')
cityCounter = Counter()
for x in table.col_values(2):
      cityCounter.update([x])
topsixLable = []
topsixValue = []
count = 0
for x in cityCounter.most_common():
    if count>5:
        if count == 6:
            topsixLable.append("其他區域")
            topsixValue.append(x[1])
        topsixValue[6] = topsixValue[6]+x[1] 
    else:
        topsixLable.append(x[0])
        topsixValue.append(x[1])
    count+=1
labels = [x for x in cityCounter]
allValue = sum([cityCounter[x] for x in cityCounter])
explode = [0 for x in range(len(topsixLable))]
sizes = [x/allValue * 100 for x in topsixValue]
import random
#colors = cm.Set1(np.arange(len(labels)))
plt.rcParams['font.sans-serif'] = ['DFKai-SB']
plt.figure(figsize=(7,9))
plt.pie(sizes,labels=topsixLable,explode=explode,labeldistance=1.2,autopct='%3.1f%%',shadow=False,startangle =90,pctdistance = 1.1)
plt.axis('equal')
plt.legend(bbox_to_anchor=(-0.1, 1.1), loc=2, borderaxespad=0.)
plt.show()
plt.savefig("city.png",format="png")
