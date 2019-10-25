
import string
from itertools import product
import re
sequence = []
def posiblesequence(a):
    for x in product(['G','C','T','A'],repeat=a):
        sequence.append(''.join(x))
    return sequence

def coverToStr(l):
    str1 = ""
    for i in l:
        str1 += i
    return str1

def indel(s, n):
    str = ''
    for i in range(len(s)):
        if (i == n):
            str += '.'
        else:
            str += s[i]
   
    return str

def matching():
    matchseq = []
    ans =[]
    string_list = input("Enter pattern ")
    pattern = string_list.split(" ")
    
    a = int(pattern[0])
    del pattern[0]
    b = int(pattern[0])
    del pattern[0]
    
    matchseq = posiblesequence(b) 
    
    print (matchseq)
    for i in matchseq:
        attempts = 0
        for j in pattern:
            word =""
            flg = False
            for n in range(b):
                word = i
                word_formed = indel(i,n)
                data = coverToStr(j)
                present = re.search(word_formed,data)
                
                if(present):
                    flg = True
                    attempts += 1
                    break

        if(attempts == a):
            ans.append(i)

    print(ans)
    
matching()