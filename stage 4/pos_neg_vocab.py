import divide_in_pos_neg

from collections import Counter

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

def divide_in_pos_neg_vocab_file(txt):

	divide_in_pos_neg.divide_in_pos_neg_textfile(txt)
	
	words = read_words("positive.txt")
	neg_words=read_words("negative.txt")

	first = []
	i=0

	count_first=[]

	for word in words:
		i=words.count(word)	
		if i>=2:
			if (word not in first):
				sttr=str(i)
				if word!='+':
					first.append(word)
					count_first.append(sttr)
		  
	file = open ("pos_vocabulary.txt","w")


	i=0
	for word in first:
		small_word=word+' '+count_first[i]+'\n'
		i += 1
		file.write(small_word)  
	

	neg = []
	i=0

	count_neg=[]

	for word in neg_words:
		i=words.count(word)
		if i>=2:
			if(word not in neg):
				nttr=str(i)
				if word!='-':
					neg.append(word)
					count_neg.append(nttr)
				
	file_neg = open ("neg_vocabulary.txt","w")

	i=0
	for word in neg:
		small_word=word+' '+count_neg[i]+'\n'
		i += 1
		file_neg.write(small_word)

	file_neg.close()
	file.close()
	return;
