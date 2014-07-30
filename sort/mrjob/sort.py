#!/usr/bin/env python
"""
Module for MRJob.
Following https://pythonhosted.org/mrjob/guides/quickstart.html
"""

from mrjob.job import MRJob

class MRWordcount(MRJob):

    def mapper(self, _, line):
        """
        Read in the line then yield as the key.
        The value is just a place holder.
        Hadoop sorts the keys (lines) before sending to the reducer.
        """
        yield (line, 1)

    # No combiner since the keys are the lines,
    # and it's very unlikely that a mapper has multiple identical lines.
    
    def reducer(self, word, counts):
        """
        Hadoop sorts the keys (lines) before sending to the reducer.
        Read in the line then yield as the key.
        The value is just a place holder.
        """
        yield (line, 1)

if __name__ == '__main__':
    MRWordcount.run()
