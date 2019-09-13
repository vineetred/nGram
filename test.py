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
# words = file.read(taleoftwocities.txt)
# f = open("twocities_test.txt", "r")
f = open("taleoftwocities.txt", "r")
words = f.read()
# words = "“Never you mind what it is!” the guard retorted. “What are you?”"
words = words.replace(".", " .")
words = words.replace("\n", " ")
words = words.replace('“', '')
words = words.split(" ")




from itertools import permutations
import random

def find_highest_freq(word_list, ngram):
    def partial_match(key, d):
        for k, v in d.items():
            if all(k1 == k2 or k2 is None  for k1, k2 in zip(k, key)):
                yield k
    mykeys = list(partial_match((word_list), what))
    subdict = {x: what[x] for x in mykeys if x in what}
    # print(subdict)
    return(max(subdict, key=subdict.get)[3])

def final(n):

    starter = "I"
    starter_1 = "am"
    starter_2 = "a"
    gibberish = []
    gibberish.append(starter)
    gibberish.append(starter_1)
    gibberish.append(starter_2)
    gibberish.append(find_highest_freq((starter,starter_1,starter_2,None),n))
    # print(gibberish)
    # print(gibberish[-1])
    # print("Im here")
    # print(gibberish)
    for i in range(0,10):
        gibberish.append(find_highest_freq((gibberish[-3],gibberish[-2],gibberish[-1], None),n))
        # starter = find_highest_freq((starter,None))
        # starter_1 = find_highest_freq((starter_1, None, None))
    print(gibberish)

n = 4
what = Counter(ngrams(words, n))
final(n)

# print(find_highest_freq(("I", )))


# def partial_match(key, d):
#     for k, v in d.items():
#         if all(k1 == k2 or k2 is None  for k1, k2 in zip(k, key)):
#             yield k

# hell = (partial_match(("Never", "you", None), what))
# print(what['Never','you','mind'])
# print(hell.next())
# print(list(hell))

# print(what["The","prisoner","wrung"])
# print(find_highest_freq(("The","prisoner",None)))