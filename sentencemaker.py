"""
Created on Sat Jul 09 17:37:51 2016
@author: Shivansh Wadhwani
"""
handle = open('wordsptr.txt')
allfile = handle.read()
allwords = allfile.split(',')
usedwords = list()

tocheck = "ILoveIceCream"

i = 0
j = 1

while True:
    wordtocheck = tocheck[i:j]
    
   # print i
    if i == len(tocheck):
        break
    
    if wordtocheck in allwords and wordtocheck not in usedwords:
        print wordtocheck
        usedwords.append(wordtocheck)
        i = j
        j = j + 1
        
    else:
        j = j + 1
        
        
print 'Done'
        
        

