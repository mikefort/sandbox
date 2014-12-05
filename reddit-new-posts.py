#imports
import praw
import pprint
import time

#setup PRAW
user_agent = ("test API please ignore")
r = praw.Reddit(user_agent=user_agent)
submissions = r.get_subreddit('all').get_new(limit=5)

for x in submissions:
	title = x.title
	subreddit = x.subreddit.display_name
	print "%s - %s" % (subreddit, title)