import praw
import random

corpus = {'<$>':{}}

corpusList = list(open("corpus.txt","r",encoding="utf8"))

for line in corpusList:
	line = line.strip('\n')
	prevWord = '<$>'
	for word in line.split():
		if word not in corpus:
			corpus[word] = {} #Adds words to selection dictionary
		if word not in corpus[prevWord]:
			corpus[prevWord][word] = 1 #Adds words to the possible words to come after prevWord
		else:
				corpus[prevWord][word] += 1
		prevWord = word

def genPost(seedWord):
	post = ''
	prevWord = seedWord
	while len(post) <= 480:
		if corpus[prevWord] == {}:
			break
		else:
			word = nextWord(prevWord)
			post += (' ' + word)
			prevWord = word
	return post

def nextWord(prevWord):
	choiceList = []
	for key in corpus[prevWord]:
		for i in range(corpus[prevWord][key]):
			choiceList.append(key)
	return random.choice(choiceList)

reddit=praw.Reddit('sandwichBot')

with open("posts_replied_to.txt", "r") as f:
	posts_replied_to = f.readlines()
	posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('sandwichsimulator')

for submission in subreddit.new(limit=1):
	if submission.id not in posts_replied_to:
		submission.reply(genPost('<$>'))
		posts_replied_to.append(submission.id)
with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + '\n')