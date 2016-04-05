import pos_neg_vocab
import re
import pickle
import divide_in_pos_neg

from collections import Counter

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()];
	
def size_of_vocab():
	count=0
	words = read_words("vocabulary.txt")
	for word in words:
		count +=1
	return count;
	
def total_count(text):
	total_frequency=0
	for f in open(text):
		f=re.sub('\n', '', f)
		word,frequency= f.split(' ')
		total_frequency+=int(frequency)
	return total_frequency;
	
def training_data(training_file):
	
	pos_neg_vocab.divide_in_pos_neg_vocab_file(training_file)
	positive_count = total_count('pos_vocabulary.txt')
	negative_count = total_count('neg_vocabulary.txt')
	probability_distribution('pos_vocabulary.txt' ,positive_count,open('positive.pickle','wb'))
	probability_distribution('neg_vocabulary.txt' ,negative_count,open('negative.pickle','wb'))
	
	
def probability_distribution(text,total_count,pickle_text):
	dict={}
	total=0
	V = size_of_vocab()
	for f in open('vocabulary.txt'):
		f=re.sub('\n', '', f)
		dict[f]=1
	for f in open(text):
		f=re.sub('\n', '', f)
		word,frequency=f.split(' ')
		dict[word]+=int(frequency)
	for i in dict:
		dict[i]=float(dict[i]+1)/float(total_count + V)
		total+=dict[i]
	pickle.dump(dict,pickle_text)
	
