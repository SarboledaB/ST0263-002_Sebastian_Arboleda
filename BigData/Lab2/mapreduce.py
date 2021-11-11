from mrjob.job import MRJob

class PromSECount(MRJob):

    def mapper(self, _, line):
      idemp, sector, salary, year = line.split(',')
      yield sector, int(salary)

    def reducer(self, sector, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield sector, avg
        
class PromEmpCount(MRJob):

    def mapper(self, _, line):
      idemp, sector, salary, year = line.split(',')
      yield idemp, int(salary)

    def reducer(self, idemp, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield idemp, avg
        
class SecEconCount(MRJob):

    def mapper(self, _, line):
      idemp, sector, salary, year = line.split(',')
      yield idemp, sector

    def reducer(self, idemp, values):
        secs = len(list(values))
        yield idemp, secs

if __name__ == '__main__':
    print('--------------------------------Punto 1--------------------------------')
    PromSECount.run()
    print('--------------------------------Punto 2--------------------------------')
    PromEmpCount.run()
    print('--------------------------------Punto 3--------------------------------')
    SecEconCount.run()