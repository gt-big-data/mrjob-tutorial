from mrjob.job import MRJob
import os

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(self, key, values):
        yield key, sum(values)

def windows_fix():
    # Windows can't make symlinks without being an Administrator.
    # Workaround: Pretend we can't make symlinks and mrjob will work without them.
    # https://github.com/Yelp/mrjob/blob/cc64250308ebf887f4dfe24959f3877a1cd31404/mrjob/sim.py#L123
    if os.name == 'nt':
        del os.symlink

if __name__ == '__main__':
    windows_fix()
    MRWordFrequencyCount.run()
