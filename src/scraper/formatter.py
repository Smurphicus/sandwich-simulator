import re

def validLine(line):
	if "[link]" in line or 'http' in line:
		return False
	return True

def probablyRealWord(word):
	ptr = 0
	count = 1
	if len(word) == 1 and word not in ['i','a']:
		return False
	while ptr < len(word)-1:
		if word[ptr] == word[ptr+1]:
			count += 1
		else:
			count = 1
		if count >= 3:
			return False
		ptr += 1
	return True

corpus = list(open("corpus.txt","r",encoding="utf8"))
newCorpus = []

for line in corpus:
	if not validLine(line):
		corpus.remove(line)
	else:
		line = re.sub(r'[:()<>{}\[\]\-_=+^@$*,.!/\"0-9]',' ',line).lower()
		line = re.sub(r'\'','', line)
		newLine = ''
		for word in line.split():
			if probablyRealWord(word):
				newLine += (word+' ')

		newCorpus.append(newLine.strip()+'\n')

with open("../poster/corpus.txt", "w",encoding='utf8') as f:
    for line in newCorpus:
        f.write(line)