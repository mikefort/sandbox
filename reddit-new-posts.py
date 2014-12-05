#!/usr/bin/env python
#imports
import praw
import pprint
import time

#setup PRAW
user_agent = ("test API please ignore")
r = praw.Reddit(user_agent=user_agent)
submissions = r.get_subreddit('all').get_new(limit=10)
#print all the things
for x in submissions:
	title = x.title
	subreddit = x.subreddit.display_name
	#make friendly
	title = title.encode('ascii', 'ignore')
	subreddit = subreddit.encode('ascii', 'ignore')
	print "%s - %s" % (subreddit, title)