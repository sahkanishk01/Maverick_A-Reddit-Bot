import praw
import pdb
import re
import json
import config
import os

def replying_jokes(posts, reddit):
	if not os.path.isfile(config.FILENAME):
		alreadyreplied = []
	else:
		with open(config.FILENAME,"r") as fi:
			alreadyreplied = fi.read()
			alreadyreplied = alreadyreplied.split("\n")
			alreadyreplied = list(filter(None, alreadyreplied))

	subreddit1 = reddit.subreddit('Jokes')
	for i in posts:
		if i.id not in alreadyreplied:
			if re.search("Joke please", i.title,re.IGNORECASE):
				for submission1 in subreddit1.hot(limit=1):
					sub1 = submission1.title
					sub2 = submission1.selftext
					i.reply("Maverick is here with a joke: "+ sub1 + " " + sub2)
				alreadyreplied.append(i.id)
	with open(config.FILENAME,"w") as fo:
		for post in alreadyreplied:
			fo.write(post + "\n")

def news(posts, reddit):
	if not os.path.isfile(config.FILENAME):
		alreadyreplied = []
	else:
		with open(config.FILENAME,"r") as fi:
			alreadyreplied = fi.read()
			alreadyreplied = alreadyreplied.split("\n")
			alreadyreplied = list(filter(None, alreadyreplied))
	subreddit2 = reddit.subreddit('indianews')
	for i in posts:
		if i.id not in alreadyreplied:
			if re.search("news headlines", i.title,re.IGNORECASE):
				for submission2 in subreddit2.new(limit=5):
					sub1 = submission2.title
					i.reply("Maverick with a news current update: "+ sub1 + "\n")
				alreadyreplied.append(i.id)
	with open(config.FILENAME,"w") as fo:
		for post in alreadyreplied:
			fo.write(post + "\n")
