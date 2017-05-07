import re

def validLine(line):
	if "[link]" in line or 'http' in line:
		return False
	return True

corpus = list(open("corpus.txt","r",encoding="utf8"))
print(corpus)

for line in corpus:
	if not validLine(line):
		corpus.remove(line)
	else:
		line = re.sub('[@$*\'\"0-9]','',line)
		print(line)