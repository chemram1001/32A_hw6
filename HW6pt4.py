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
		self.stoplist = []
		for line in self.stopfile:
			line = line.replace("'", "")
			line = line.rstrip()
			#line = self.stopfile.readline()
			self.stoplist.append(line)
			#print(line)
		#self.stopwordslist = list(self.stopfile)
#		print(self.stoplist)
#		print(len(self.stoplist))

	def incCount(self,text):
		text = text.lower()
		translator = str.maketrans( '' , '', string.punctuation)
		text = text.translate(translator)
		#text = text.strip(string.punctuation)
		#text = clean(text)
		text = text.split()
		#print(text)
		if text == "":
			#return (self.wordCounts)
			pass
		for i in text:
			if i in self.stoplist:
				pass
			else:
				if (i in self.wordCounts) == False:
					self.wordCounts[i] = 1
				else:
					self.wordCounts[i] += 1
		return (self.wordCounts)

	def lookUpCount(self,lookword):
		if lookword in self.wordCounts:
			print(self.wordCounts[lookword])
		else:
			print(0)

	def getTopWords(self,number):
		wordList = []	# make dictionary into list of tuples
		for (key, value) in self.wordCounts.items():
			pairs = (value,key)
			wordList.append(pairs)
			#print(pairs)
		#wordList = sorted(wordList,key=lambda tup: tup[1]).reverse()
		wordList = sorted(wordList, key=lambda tup: tup[0], reverse = True)
		#print(wordList)
		num = []
		for i in range(number):
			num.append(wordList[i])
		return num
def main():
	counter = Count()  #make a counter object from class count
	story = open("Alice.txt",'r')	# open the file alice.txt to read it
	wordlist= list(story)	# create a word list from the file
	for words in wordlist:	# loop through the words in the word list
		counter.incCount(words)	# add all words to wordCount dictionary
	#counter.lookUpCount("alice")
	#counter.lookUpCount("rabbit")
	#counter.lookUpCount("and")
	#counter.lookUpCount("she")
	counter.lookUpCount("well")

	#test code for getTopLines
	topTen = counter.getTopWords(10)
	print(topTen)

main()
