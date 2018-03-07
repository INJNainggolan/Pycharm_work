#-*- 从丁：utf-8 -*-

import pandas as pd

inputfile = 'huizong.csv'
outputfile = 'iPhoneX.txt'
data = pd.read_csv(inputfile, encoding='utf-8')
data = data[[u'评价内容']][data[u'评价星级'] == u'star5']
data.to_csv(outputfile, index=False, header=False)