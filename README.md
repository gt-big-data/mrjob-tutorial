# [mrjob](https://pythonhosted.org/mrjob/index.html)
Run MapReduce jobs locally and on the cloud
## Installation
<pre><code>pip install mrjob
</code></pre>
## Basic MapReduce job
Open a new python file and name it wordcount.py
<pre><code>from mrjob.job import MRJob


class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRWordFrequencyCount.run()
</code></pre>
