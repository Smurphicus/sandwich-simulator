import praw

corpusList = []

with open("../scraper/corpus.txt","r") as corpusText:
	corpusList = corpusText.readlines()

def genPost(){
	
}

reddit=praw.Reddit('sandwichBot')

with open("posts_replied_to.txt", "r") as f:
	posts_replied_to = f.readlines()
	#posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('sandwichsimulator')

for submission in subreddit.hot(limit=2):
	if submission.id not in posts_replied_to:
		if "beep" in submission.title.lower():
			submission.reply("Beep boop I'm a bot!")
			posts_replied_to.append(submission.id)
with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")