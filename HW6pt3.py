# ECS 32A
# Assignment 6
# Word Counting Class
from wordle import wordleFromObject
from cleanWord import clean
import string
class Count:
	wordCounts = None
	def __init__(self):
		print("Initializing Word Counter")
		self.wordCounts = {}
		self.stopfile = open("stopWords.txt",'r')
		self.stopwordslist = list(self.stopfile)
		#print(self.stopwordslist)

	def incCount(self,text):
		text = text.lower()
		translator = str.maketrans( '' , '', string.punctuation)
		text = text.translate(translator)
		#text = text.strip(string.punctuation)
		#text = clean(text)
		text = text.split()
		#print(text)
		if text == "":
			return (self.wordCounts)
		for i in text:
			if i in self.stopwordslist:
				break
			else:
				if (i in self.wordCounts) == False:
					self.wordCounts[i] = 1
				else:
					self.wordCounts[i] += 1
		return (self.wordCounts)

	def lookUpCount(self,i):
		if i in self.wordCounts:
			print(self.wordCounts[i])
		else:
			print(0)
def main():
	counter = Count()  #make a counter object from class count
	story = open("Alice.txt",'r')	# open the file alice.txt to read it
	wordlist= list(story)	# create a word list from the file
	for words in wordlist:	# loop through the words in the word list
		counter.incCount(words)	# add all words to wordCount dictionary
	counter.lookUpCount("alice")
	counter.lookUpCount("rabbit")
	counter.lookUpCount("and\n")
	counter.lookUpCount("she\n")


main()
