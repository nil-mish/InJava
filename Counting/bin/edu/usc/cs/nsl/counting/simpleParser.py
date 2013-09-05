import sys
import re

the_lines = sys.stdin.readlines()

for each_line in the_lines:
	results = re.findall(r'\b\w+\b', each_line, re.I)
	for each_word in results:
		print each_word
