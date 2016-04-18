import train
import pickle
import math
import re

def vocab_size():
    count=0
    for f in open('vocabulary_bigram.txt'):
        count+=1
    return count

def prior_probability(training_set):
    positive=negative=0
    for f in training_set:
        if f.split(' ')[0]=='+':
            positive+=1
        else:
            negative+=1
    return positive,negative

def find_total_count(text):
    total_frequency=0
    for f in open(text):
        f=re.sub('\n', '', f)
        if f.count(' ')==1:
            word,frequency= f.split(' ')
            total_frequency+=int(frequency)
        else:
            word1,word2,frequency=f.split(' ')
            total_frequency+=int(frequency)
    return total_frequency
	

def file_size():
    count=0
    for f in open('stage2_result.txt'):
        count+=1
    return count


def test(training_set,test_set,positive_count,negative_count):
    vocab=[]
    positive_dict = pickle.load(open('positive_bigram.pickle','rb'))
    negative_dict = pickle.load(open('negative_bigram.pickle','rb'))
    correct=tp=tn=fp=fn=0
    positive_prior,negative_prior=prior_probability(training_set)
    for f in open('vocabulary_bigram.txt'):
        f=re.sub('\n', '', f)
        vocab.append(f)
    for f in test_set:
        f=f.strip()
        words=f.split(' ')[1:]
        positive_probability=0
        negative_probability=0
        for i in range(len(words)-1):
            string=words[i]+ ' ' + words[i+1]
            if string in vocab:
                positive_probability+=math.log(positive_dict[string])
                negative_probability+=math.log(negative_dict[string])
            else:
                size=vocab_size()
                if words[i] in vocab:
                     positive_probability+=math.log(positive_dict[words[i]])
                     negative_probability+=math.log(negative_dict[words[i]])
                else:
                    temp=1.0/(positive_count+size)
                    positive_probability+=math.log(temp)
                    temp=1.0/(negative_count+size)
                    negative_probability+=math.log(temp)
                if words[i+1] in vocab:
                    positive_probability+=math.log(positive_dict[words[i+1]])
                    negative_probability+=math.log(negative_dict[words[i+1]])
                else:
                        temp=1.0/(positive_count+size)
                        positive_probability+=math.log(temp)
                        temp=1.0/(negative_count+size)
                        negative_probability+=math.log(temp)
        positive_probability+=math.log(positive_prior)
        negative_probability+=math.log(negative_prior)
        if(positive_probability>negative_probability):
            if(f.split(' ')[0]=='+'):
                correct+=1
                tp+=1
            else:
                fp+=1
        else:
            if f.split(' ')[0] == '-':
                correct += 1
                tn+=1
            else:
                fn+=1
    return correct,tp,tn,fp,fn


def cross_validation():
	list=[]
	total_accuracy=0
	fold_size=file_size()//10
	fileee=open('stage2_result.txt')
    
	for f in fileee:
		f=re.sub('\n', '', f)
		list.append(f)
	fileee.close()	
	
	
	for i in range(9,-1,-1):
		test_set=list[i*fold_size:][:fold_size]
		training_set=list[0:i*fold_size] + list[(i+1) * fold_size:]
		train.train(training_set)
		correct,tp,tn,fp,fn=test(training_set,test_set,find_total_count('vocabulary_bigram_positive.txt'),find_total_count('vocabulary_bigram_negative.txt'))
		accuracy = float(tp+tn)/float(tp+tn+fp+fn)
		print (accuracy*100)
		total_accuracy+=accuracy
	print ((total_accuracy/10)*100)

cross_validation()