import re


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
f = open("taleoftwocities.txt", "r")
words = f.read()
# words = "“Never you mind what it is!” the guard retorted. “What are you?”"
words = words.replace(".", " .")
words = words.replace("\n", " ")
words = words.replace('“', '')
words = words.split(" ")




from itertools import permutations
import random

def find_highest_freq(word_list, ngram, what):
    def partial_match(key, d):
        for k, v in d.items():
            if all(k1 == k2 or k2 is None  for k1, k2 in zip(k, key)):
                yield k
    mykeys = list(partial_match((word_list), what))
    subdict = {x: what[x] for x in mykeys if x in what}
    # print(subdict)
    # try:
    return(max(subdict, key=subdict.get)[n-1])
    # except:
    #     return find_highest_freq(starter)

def final(starter,starter_1,starter_2,n, wordslist):
    gibberish = []
    # starter = "I"
    gibberish.append(starter)
    if(starter_1!=None):
        gibberish.append(starter_1)
    if(starter_2!=None):
        gibberish.append(starter_2)
    print(gibberish)
    try:
        gibberish.append(find_highest_freq((starter,starter_1,starter_2,None),n,wordslist))
    except:
        try:
            gibberish.append(find_highest_freq((starter,starter_1,None,None),(n-1),wordslist))
        except:
            gibberish.append(find_highest_freq((starter,None,None,None),(n-2),wordslist))

    for i in range(0,10):
        try:
            gibberish.append(find_highest_freq((gibberish[-3],gibberish[-2],gibberish[-1], None),n,wordslist))
        except:
            try:
                gibberish.append(find_highest_freq((gibberish[-3],gibberish[-2],None, None),(n-1),wordslist))
            except:
                gibberish.append(find_highest_freq((gibberish[-3],None,None, None),(n-2),wordslist))
    print(gibberish)

n = 3
what_4 = Counter(ngrams(words, 3))
# what_3 = Counter(ngrams(words,3))
# what_2
final("And", "having",None, n, what_4)
