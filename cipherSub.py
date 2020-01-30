#!/usr/bin/python2.7

import sys

# read Ciphertext from arguments  
if len(sys.argv) < 2:
    ciphertext = "pfmmwpwskmmsfjppfkkms"
else:
    ciphertext = ' '.join(sys.argv[1:])


# Count of Characters in cipher text
charCount = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0} 

 
for keys in ciphertext: 
    charCount[keys] = charCount.get(keys,0) + 1


print("\n\nLetter Occurences in Cipher Text:"+str(charCount))

sortedList = sorted(charCount , key=charCount.__getitem__, reverse=True)

print("\n\nSorted Letter Occurences in Cipher Text:"+str(sortedList))

letterFreqSorted=['E','T','A','O','I','N','S','H','R','D','L','C','U','M','W','F','G','Y','P','B','V','K','J','X','Q','Z']


# from sorted frequency Array and Sorted occurence array get the possible cipher key array 
mapArr = {}

i=0
for keys in sortedList:
      mapArr[keys]=letterFreqSorted[i];
      i=i+1

# sort the array to get the cipher key
mapArrSorted= sorted(mapArr, key=mapArr.__getitem__); 

print("\n\n Mapping Array:"+str(mapArrSorted)); 


# get cipher Key text
cipherKey = '';
i=0
for keys in mapArrSorted:
    cipherKey=cipherKey+mapArrSorted[i];
    i=i+1

print("\n\nCipher Key:"+cipherKey);

print("\n\n************Deciphered Text************\n\n")

decipherText = ''

for keys in ciphertext:
      decipherText=decipherText+mapArr[keys]

print("Deciphered Text:"+decipherText)

print("\n\n************Deciphered Text************\n\n")

