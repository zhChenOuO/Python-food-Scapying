import xlrd
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
colors = ["red","coral","green","yellow","orange","purple","Indigo"]
data = xlrd.open_workbook('dataFood.xlsx')
table = data.sheet_by_name(u'愛評網')
cityCounter = Counter()
for x in table.col_values(1)[1:]:
      cityCounter.update([x])
labels = [x for x in cityCounter]
allValue = sum([cityCounter[x] for x in cityCounter])
explode = [0 for x in range(len(labels))]
sizes = [cityCounter[x]/allValue * 100 for x in cityCounter]
import random
#colors = cm.Set1(np.arange(len(labels)))
plt.rcParams['font.sans-serif'] = ['DFKai-SB']
plt.figure(figsize=(7,9))
plt.pie(sizes,labels=labels,explode=explode,labeldistance=1.2,autopct='%3.1f%%',shadow=False,startangle =90,pctdistance = 1.1)
plt.axis('equal')
plt.legend(bbox_to_anchor=(-0.1, 1.1), loc=2, borderaxespad=0.)
plt.show()
plt.savefig("city.png",format="png")
