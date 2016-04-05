import testing
import multinomial_model
import re

def prior_probability(training_set):
    positive=negative=0
    for f in training_set:
        if f.split(' ')[0]=='+':
            positive+=1
        else:
            negative+=1
    return positive,negative

def size_of_file():
    count=0
    for f in open('stage2_result.txt'):
        count+=1
    return count;



def cross_validation():
	list=[]
	tot_accuracy=0
	fold_size=size_of_file()//10
	fileee=open('stage2_result.txt')
    
	for f in fileee:
		f=re.sub('\n', '', f)
		list.append(f)
	fileee.close()	
	
	for i in range(9,-1,-1):
		test_set=list[i*fold_size:][:fold_size]
		training_set=list[0:i*fold_size] + list[(i+1) * fold_size:]
		
		with open('training_set.txt', 'w') as f:
			for s in training_set:
				f.write(s + '\n')
			f.close()
		
		multinomial_model.training_data('training_set.txt')
		correct,tp,tn,fp,fn=testing.test(training_set,test_set)
		accuracy = float(tp+tn)/float(tp+tn+fp+fn)
		print (accuracy*100)
		tot_accuracy+=accuracy
	print ((tot_accuracy/10)*100)

cross_validation()