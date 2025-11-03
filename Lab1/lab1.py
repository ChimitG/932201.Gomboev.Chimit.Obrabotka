import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
import pymorphy3
nltk.download('punkt')
nltk.download('punkt_tab')
file = open('Text.txt','r', encoding='utf-8')
content = file.read()
file.close()
m = pymorphy3.MorphAnalyzer()
sent = sent_tokenize(content)
tok = []
for i in sent:
    tok.append(word_tokenize(i))
pairs = []
for word in tok:
    for l in range(len(word)-1):
        wordFirst = m.parse(word[l])[0]
        wordSecond = m.parse(word[l+1])[0]
        tagfirst = wordFirst.tag
        tagsecond = wordSecond.tag
        if (tagfirst.POS == 'NOUN' or tagfirst.POS == 'ADJF') and (tagsecond.POS == 'NOUN' or tagsecond.POS == 'ADJF'):
            if (tagfirst.gender == tagsecond.gender):
                if (tagfirst.number == tagsecond.number):
                    if (tagfirst.case == tagsecond.case):
                        pairs.append(wordFirst.normal_form + " " + wordSecond.normal_form)
for pair in pairs:
    print(pair)
