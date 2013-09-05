import sys

a_set = set('')


a_file = open(sys.argv[1],'r')

a_line = a_file.readline()
while(a_line):
	if(a_line.strip() in a_set):
		print(a_line)
	else:
		a_set.add(a_line.strip())
	a_line = a_file.readline()
