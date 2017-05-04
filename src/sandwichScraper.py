import praw

reddit = praw.Reddit('sandwichBot')

subreddit = reddit.subreddit("sandwichsimulator")

for submission in subreddit.hot(limit=2):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    comments = submission.comments
    for comment in comments:
    	print("Comment: ", comment.body)
    	print("------------------------\n")

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")