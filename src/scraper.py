import praw

reddit = praw.Reddit('sandwichBot')

subreddit = reddit.subreddit("sandwiches")

corpus = []

for submission in subreddit.hot(limit=250):
    corpus.append(submission.selftext)
    comments = submission.comments
    for comment in comments:
    	corpus.append(comment.body)

with open("corpus.txt", "w",encoding='utf8') as f:
    for message in corpus:
        f.write(message + "\n")