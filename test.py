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
# words = re.findall("(\w+)|.]", "I am Sam. I am Vineet.")
# words = "I am Sam. I am Vineet. I like to go fishing. I would love to go to the mountains. Vineet loves this. Vineet loves this."
words = file.read(taleoftwocities.txt)
words = words.replace(".", " .").split(" ")
# print(words)
# words = words.split(" ")
what = Counter(ngrams(words, 2))
# print(ngrams(words,2))
# print(list(what))
# for k, v in what.items():
#     print(k)

# print(what['I',])
# print(what.keys())
# any(key.startswith("Vineet") for key in what)
# print(max(what, key=what.get))
# any(key.startswith('Vineet') for key in what)
# for key in what:
#     print(key.startswith("Vineet"))
from itertools import permutations
import random

def find_highest_freq(word_list):
    def partial_match(key, d):
        for k, v in d.iteritems():
            if all(k1 == k2 or k2 is None  for k1, k2 in zip(k, key)):
                yield k
    mykeys = list(partial_match((word_list), what))
    subdict = {x: what[x] for x in mykeys if x in what}
    return(max(subdict, key=subdict.get)[1])
    
# find_highest_freq(('Vineet', None))
starter = 'Vineet'
gibberish = []
gibberish.append(starter)
for i in range(0,3):
    gibberish.append(find_highest_freq((starter,None)))
    starter = find_highest_freq((starter,None))
# print(''.join(gibberish))
print(gibberish)

    
# print(what.get)