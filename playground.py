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
    if not mykeys:
        word_list = list(word_list)
        del word_list[-2]
        # del word_list[-1]
        # print(word_list)
        mykeys = list(partial_match((word_list), what_3))
        subdict = {x: what[x] for x in mykeys if x in what_3}
        print(subdict)
        return(max(subdict, key=subdict.get)[n-2])
    print(mykeys)
    subdict = {x: what[x] for x in mykeys if x in what}
    return(max(subdict, key=subdict.get)[n-1])


def final(starter,starter_1,starter_2,n, wordslist):
    gibberish = []
    # starter = "I"
    gibberish.append(starter)
    if(starter_1!=None):
        gibberish.append(starter_1)
    if(starter_2!=None):
        gibberish.append(starter_2)
    print(gibberish)
    gibberish.append(find_highest_freq((starter,starter_1,starter_2,None),n,wordslist))

    for i in range(0,10):
        gibberish.append(find_highest_freq((gibberish[-3],gibberish[-2],gibberish[-1], None),n,wordslist))
    print(gibberish)

n = 4
what_4 = Counter(ngrams(words, 4))
what_3 = Counter(ngrams(words, 3))
# final("and", "having","got", n, what_4)
import string
def punc(text):
    outputText = []
    for word in text:
        if word == "!" or word == "," or word == "\\”" or word == "?":
            word = ""
        outputText += [word]
    return outputText
str = 'What are you?'
print(punc(str))
