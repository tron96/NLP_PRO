import re
 
def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]
 
data_file = open('data.txt', 'r')
stopwords = read_words("stopwords.txt")
result_file = open('stage2_result.txt', 'w')
 
line = data_file.readline()
 
 
 
while line:
	line = line.lower()
	tag = line[0]
	new_line=re.sub('[^a-zA-Z\n  ]',' ', line)
	new_line=re.sub('[  ]+',' ',new_line)
	new_line=re.sub(' '+'[a-zA-Z]'+' ',' ',new_line)
	new_line=re.sub(' '+'[a-zA-Z]'+' ',' ',new_line)
	new_line=re.sub(' '+'[a-zA-Z]'+'\n','\n',new_line)
	new_line=re.sub(' '+'ll'+' ',' ',new_line)
	
	for s_word in stopwords:
		new_line = re.sub(' ' + s_word + ' ', ' ', new_line)
		new_line = re.sub(' ' + s_word + '\n', '\n', new_line)
		new_line = re.sub(' ' + s_word + ' ', ' ', new_line)
		
	
	result_file.write(tag + '' + new_line)
	line = data_file.readline()

	
data_file.close()
result_file.close()
		
	