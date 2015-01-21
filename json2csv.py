#!usr/bin/env python

import json
import codecs
import unicodecsv
import sys

article = codecs.open('collect_data/data/article.dat','r', 'utf-8')
header = []
count_dict = {} # used to remove unused column
count_record = 0.0
for line in article:
  j = json.loads( line.rstrip() )
  for key in j:
    if key not in header:
      header.append(key)
      count_dict[key] = 0

# generate new article file
article = codecs.open('collect_data/data/article.dat','r', 'utf-8')
new_article = codecs.open('article.new.dat','w','utf-8')
for line in article:
  str_j = u'{'
  j = json.loads(line.rstrip())
  for h in header:
    if h not in j:
      j[h] = u'' 
  for idx,key in enumerate(j):
    str_j += u'"' + key + u'":'
    if isinstance(j[key], list): 
      count_dict[key] += 1
      str_j += u'[' 
      new_value = []
      for idx_e,elem in enumerate(j[key]):
        if len(j[key]) == idx_e+1:
          str_j += u'"' + elem + u'"'
        else:
          str_j += u'"' + elem + u'",'
      str_j += u'],'
    else:
      if j[key] != u'':
        count_dict[key] += 1
      if len(j) == idx+1:
        str_j += u'"' + j[key] + u'"'
      else:
        str_j += u'"' + j[key] + u'",'
  str_j += u'}\n'
  #print str_j
  new_article.write(str_j)
  count_record += 1
    
# write new article file to csv
f = unicodecsv.writer(open('test.csv', 'wb'), encoding='utf-8')
article = codecs.open('article.new.dat','r', 'utf-8')

# conditionally filter out unsatisfied features
if len(sys.argv) > 1:
  header = [h for h in header if count_dict[h]/count_record > float(sys.argv[1])]
else:
  header = [h for h in header if count_dict[h] >0]
f.writerow(header) # write header first

for line in article:
  j = json.loads( line.rstrip() )
  row = []
  for key in header:
    if isinstance(j[key], list): 
      seq = '&'.join(j[key])
      row.append(seq.encode('utf-8'))
    else:
      row.append(j[key].encode('utf-8'))
  f.writerow(row)

print 'SUCCESS'
