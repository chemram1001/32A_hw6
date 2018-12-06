# ECS 32A
# Assignment 6
#
# Word Counting Class
from wordle import wordleFromObject
from cleanWord import clean
import string
class Count:
	wordCounts = None
	def __init__(self):
		print("Initializing Word Counter")
		self.wordCounts = {}

	def incCount(self,text):
		text = text.lower()
		translator = str.maketrans( '' , '', string.punctuation)
		text = text.translate(translator)
		text = text.split()
		#print(text)
		if text == "":
			return
		for i in text:
			if (i in self.wordCounts) == False:
				self.wordCounts[i] = 1
			else:
				self.wordCounts[i] += 1
		#print(self.wordCounts)

	def lookUpCount(self,i):
		if i in self.wordCounts:
			print(self.wordCounts[i])
		else:
			print(0)
def main():
	counter = Count()
	counter.incCount("well Well WELL, if it isn't little little ")
	counter.lookUpCount("if")
	counter.lookUpCount("little")
	counter.lookUpCount("...")
	counter.lookUpCount("pizza")
main()
