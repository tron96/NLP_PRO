import re
import pickle

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

def vocab_size():
    count=0
    for f in open('vocabulary_bigram.txt'):
        count+=1
    return count

def create_vocab(training_set,file,char):
    vocabulary_unigram=[]
    vocabulary_bigram=[]
    f1=open(file,'w')
    for f in training_set:
        if(f.split(' ')[0]==char):
            f=f.strip()
            words = f.split(' ')[1:]
            for i in range(len(words)-1):
                vocabulary_unigram.append(words[i])
                vocabulary_bigram.append(words[i]+' '+words[i+1])
            vocabulary_unigram.append(words[-1])
    vocabulary_bigram=[x for x in vocabulary_bigram if vocabulary_bigram.count(x)>=3]
    vocabulary_unigram=[x for x in vocabulary_unigram if vocabulary_unigram.count(x)>=2]
    sorted_set_unigram=sorted(set(vocabulary_unigram))
    sorted_set_bigram=sorted(set(vocabulary_bigram))
    for i in sorted_set_unigram:
        sub=0
        for j in sorted_set_bigram:
                word1,word2=j.split(' ')
                if word1==i or word2==i:
                    sub+=vocabulary_bigram.count(j)
        if (vocabulary_unigram.count(i)-sub)>=2 and len(i)>1:
            f1.write(i + ' ' + str(vocabulary_unigram.count(i)-sub) + '\n')

    for i in sorted_set_bigram:
         if len(str(i).split())!=1 and len(i)>1:
            f1.write(i + ' ' + str(vocabulary_bigram.count(i)) + '\n')

def create_probability_distribution(text,tot_count,pickle_text):
    dict={}
    total=0
    v = vocab_size()
    for f in open('vocabulary_bigram.txt'):
        f=re.sub('\n', '', f)
        dict[f]=1
    for f in open(text):
        f=re.sub('\n', '', f)
        if f.count(' ')==1:
            word,frequency=f.split(' ')
            dict[word]+=int(frequency)
        else:
            word1,word2,frequency=f.split(' ')
            dict[word1+' '+word2]+=int(frequency)
    for i in dict:
        dict[i]=float(dict[i])/float(tot_count + v)
        total+=dict[i]
    pickle.dump(dict,pickle_text)

def train(training_set):
    create_vocab(training_set,'vocabulary_bigram_positive.txt','+')
    create_vocab(training_set,'vocabulary_bigram_negative.txt','-')
    total_positive_count = find_total_count('vocabulary_bigram_positive.txt')
    total_negative_count = find_total_count('vocabulary_bigram_negative.txt')
    create_probability_distribution('vocabulary_bigram_positive.txt' ,total_positive_count, open('positive_bigram.pickle','wb'))
    create_probability_distribution('vocabulary_bigram_negative.txt' ,total_negative_count,open('negative_bigram.pickle','wb'))
