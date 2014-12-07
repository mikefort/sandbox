#!/usr/bin/env python
#imports
import praw
import time
import pprint

#setup PRAW
user_agent = ("test API please ignore")
r = praw.Reddit(user_agent=user_agent)
posts = r.get_subreddit('all').get_hot(limit=10)
#print all the things
for x in posts:
	title = x.title
	subreddit = x.subreddit.display_name
	url = x.url
	#make friendly
	title = title.encode('ascii', 'ignore')
	subreddit = subreddit.encode('ascii', 'ignore')
	url = url.encode('ascii', 'ignore')
	print "%s - %s : %s" % (subreddit, title, url)