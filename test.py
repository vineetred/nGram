# import pandas as pd
import re
# # data = pd.read_csv('taleoftwocities.txt')
# f = open("taleoftwocities.txt", "r")
# data = f.readlines()
# k = 0
# word = 'cut short'


# # for line in data:
# #     # line = line.split()
# #     for i in line:
# #         if(i==word):
# #             k=k+1
# # # print(k)
# strr = 'OMG is this a question! Is this a senetence?'
# pat = re.compile(r'([A-Z][^\.!?]*[\.!?])',re.M)
# occurence = re.findall(pat, strr)
# print(occurence)

from itertools import tee, islice
from collections import Counter 

def ngrams(lst, n):
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break
words = re.findall("\w+", "I am Sam. Sam I am. I do not like green eggs and ham.")
print(Counter(ngrams(words, 2)))
