#!/usr/bin/env python

from mrjob.job import MRJob
from mrjob.step import MRStep
import re

from pprint import PrettyPrinter

pp = lambda x : PrettyPrinter(indent = 2).pprint(x)

class MRBigram(MRJob):

    SORT_VALUES = True

    def combine_counts(self, key, counts):
        yield key, sum(counts)

    def mapper(self, _, line):
        def normalize(text):
            words = re.compile(r"[\w']+").findall(text)
            words = [word.lower() for word in words]
            return [word for word in words if not word.isdigit()]

        data = line.split(',')

        lineNumber = data[0]
        text = data[1]
        corpus = normalize(
            text[1:-1] if (text.startswith('"') and text.endswith('"')) else text
        )

        previous_word = None
        for word in corpus:
            if previous_word is not None:
                yield (previous_word, '##SELF##'), 1
                yield (previous_word, word), 1

            previous_word = word

    def reducer(self, previous_word, value):
        occurrence = 0.0

        for id, data in value:
            if 'total_01' == id:
                occurrence = float(data)
            elif 'total_02' == id and 'my' == previous_word:
                yield (100.0 * float(data[1]) / occurrence, data[0])

    def steps(self):
        return [
            MRStep(mapper=self.mapper, combiner=self.combine_counts, reducer=self.summarise_counts),
            MRStep(reducer=self.reducer)
        ]

    def summarise_counts(self, key, counts):
        previous_word, word = key
        count = sum(counts)

        if '##SELF##' == word:
            yield previous_word, ('total_01', count)
        else:
            yield previous_word, ('total_02', (word, count))

if __name__ == '__main__':
    MRBigram.run()
