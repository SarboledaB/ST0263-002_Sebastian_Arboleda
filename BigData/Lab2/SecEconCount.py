from mrjob.job import MRJob

class SecEconCount(MRJob):

    def mapper(self, _, line):
      idemp, sector, salary, year = line.split(',')
      yield idemp, sector

    def reducer(self, idemp, values):
        secs = len(list(values))
        yield idemp, secs

if __name__ == '__main__':
    SecEconCount.run()