import string
import math
import re

# with open('cmn_en/cmn.txt','r', encoding='utf-8') as f:
#   for i in range(5):
#     line = f.readline()
#     line = line.split('\t')[0:2]
#     line = '\t'.join(line)
#     line = line + '\n'
#     print(line)

from_file = open('cmn_en/cmn.txt', 'r', encoding='utf-8')
to_file = open('cmn_en/cmn_proc.txt','w',encoding='utf-8')
cnt = 0

for line in from_file:
    line = line.split('\t')[0:2]
    line = '\t'.join(line)
    line = line + '\n'
    to_file.writelines(line)
    cnt += 1
to_file.close()
from_file.close()
print(cnt)