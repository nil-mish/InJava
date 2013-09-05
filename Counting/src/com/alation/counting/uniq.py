import sys

a_set = set('')
b_set = set('')

a_file = open(sys.argv[1],'r')

a_line = a_file.readline()
while(a_line):
	a_set.add(a_line.strip())
	a_line = a_file.readline()
a_file.close()

b_file = open(sys.argv[2],'r')

b_line = b_file.readline()
while(b_line):
	b_set.add(b_line.strip())
	b_line = b_file.readline()

c_set = b_set - a_set

d_set = a_set - b_set

print(len(a_set), len(b_set), len(c_set), len(d_set))
