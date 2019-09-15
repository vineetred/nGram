import string
from collections import Counter 
from itertools import tee, islice


def load_Text(text_Name):


    def full_Stop_Remove(text):
        outputText = []
        for word in text:
            if word == "!" or word == "," or word == "\\”" or word == "?":
                word = ""
            outputText += [word]
        return outputText

    text_WITHPUNC = open("taleoftwocities.txt", "r", encoding="utf8").read().lower()
    text_WITHPUNC = text_WITHPUNC.replace("\n", " ").replace("."," .").replace('"', '').split(" ")
    text_1 = full_Stop_Remove(text_WITHPUNC)
    text_2_WITHPUNC = open("Warandpeace.txt", "r", encoding="utf8").read().lower()
    text_2_WITHPUNC = text_2_WITHPUNC.replace("\n", " ").replace("."," .").replace('"', '').split(" ")
    text_2 = full_Stop_Remove(text_2_WITHPUNC)
    if(text_Name == "War And Peace"):
        return text_2
    else:
        return text_1



def n_Gram_Creator(lst, n):
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

def word_Predictor(fileName, start, n, word_BLOCKS_Length):
    
    start = start.split(" ")
    word_BLOCKS = start
    Ngrams = Counter(n_Gram_Creator(fileName, n)) 

    for i in range(0, word_BLOCKS_Length):
        prefix = word_BLOCKS[max(0, len(word_BLOCKS)-n+1):max(len(word_BLOCKS), 1)]
        sum = 0
        max_Sum = ""
        word_Bool = False
        for wordGroup in Ngrams.keys():

            if list(wordGroup[0:len(wordGroup)-1]) == prefix and Ngrams[wordGroup]>sum and not(i<10 and wordGroup[-1] == ".") and not(wordGroup[-n:] in word_BLOCKS):    
                max_Sum = wordGroup[-1]
                sum = Ngrams[wordGroup]
                word_Bool = True
                # STOP SEARCHING PLS
        
        if word_Bool == False:
            word_BLOCKS_String =" ".join(word for word in word_BLOCKS)
            word_BLOCKS = word_Predictor(fileName, word_BLOCKS_String, n-1, 1)
            continue

        if max_Sum != ".":
            word_BLOCKS = word_BLOCKS + [max_Sum.translate(str.maketrans('', '', string.punctuation))]
        else:
            # If full stop before 10 words, find second highest.
            word_BLOCKS = word_BLOCKS + [max_Sum]
    return word_BLOCKS


ONE = "i suppose"
TWO = "and having got"
THREE = "not two minutes"


text_1 = load_Text("Tale of Two cities")
enchoate = word_Predictor(text_1, ONE, 4, 30)
final_Output = " ".join(enchoate)
print(final_Output)
