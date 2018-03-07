#-*- coding: utf-8 -*-
import pandas as pd

inputfile = 'iPhoneX.txt'
outputfile = 'iPhone_process_1.txt'
data = pd.read_csv(inputfile, encoding='utf-8', header=None)
l1 = len(data)
data = pd.DataFrame(data[0].unique())
l2 = len(data)
data.to_csv(outputfile, index=False, header=False, encoding='utf-8')
print(u'删除了%s条评论。'%(l1 - l2))