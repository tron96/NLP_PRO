import pickle
import re
import math

def prior_probability(training_set):
    positive=negative=0
    for f in training_set:
        if f.split(' ')[0]=='+':
            positive+=1
        else:
            negative+=1
    return positive,negative

def test(training_set,test_set):
    vocab=[]
    positive_dict = pickle.load(open('positive.pickle','rb'))
    negative_dict = pickle.load(open('negative.pickle','rb'))
    correct=tp=tn=fp=fn=0
    positive_prior,negative_prior=prior_probability(training_set)
    for f in open('vocabulary.txt'):
        f=re.sub('\n', '', f)
        vocab.append(f)
    for f in test_set:
        words=f.split(' ')
        sentiment = f.split(' ')[0]
        positive_probability=0
        negative_probability=0
        for i in words:
            if i in vocab:
                positive_probability+=math.log(positive_dict[i])
                negative_probability+=math.log(negative_dict[i])
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