
def divide_in_pos_neg_textfile(txtfile):
	
	fname=txtfile
	data_file = open(fname,'r')

	positive_data_file = open('positive.txt', 'w')
	negative_data_file = open('negative.txt', 'w')

	line = data_file.readline()

	while line:
		tag = line[0]
		if tag=='+':
			positive_data_file.write(line)
		else :
			negative_data_file.write(line)
			
		line = data_file.readline()
	
	positive_data_file.close()
	negative_data_file.close()
	data_file.close()
	
	return;
	
