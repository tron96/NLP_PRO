from collections import Counter
def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]
words = read_words("stage2_result.txt")

first=[]



for word in words:
   i=words.count(word)
   if i>=2:
      if (word not in first):
          first.append(word)


		  
		  

first.sort()		  


first.remove('+')
first.remove('-')
 
file = open ("vocabulary.txt","w")

for word in first:
    small_word=word+ '\n'
    file.write(small_word)   

