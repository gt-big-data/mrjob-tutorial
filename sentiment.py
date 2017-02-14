from mrjob.job import MRJob
import re

class MRSentiment(MRJob):

	def mapper_init(self):
		self.weights = {}
		with open("sentiments.txt", "r") as f:
			for line in f:
				ls = re.split('\s+', line.strip().lower())
				if len(ls) == 2:
					word = ls[0]
					word = re.sub('\W', '', word)
					self.weights[word] = float(ls[1])

	def mapper(self, _, line):
		ls = line.lower().split()
		count = 0
		for word in ls:
			if word in self.weights:
				count += self.weights[word]
		yield line, count

	def reducer(self, key, values):
		tot, n = 0.0, 0.0
		for value in values:
			n += 1
			tot += value
		yield (key, tot/n)

if __name__ == '__main__':
	MRSentiment.run()