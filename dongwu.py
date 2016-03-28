class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):
        return Chain('%s/%s' %(self._path,path))
    def __str__(self):
        return self._path
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10000:
            raise StopIteration();
        return self.a
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            a,b=1,1
            l=[]
            for x in range(stop):
                if x>=start:
                    l.append(a)
                a,b=b,a+b
            return l

    def __getattr__(self,attr):
        if attr=='age':
            return lambda:25
 
class Animal(object):
    def run(self):
        print 'I can run!'
    def __len__(self):
        return 100
class Dog(Animal):
    def run(self):
        print 'Dog can running!'
    def shout(selft):
        print 'Dog can shout!'

class Cat(Animal):
    pass

class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score):
        if isinstance(score,int):
            if score<0 or score>100:
                raise ValueError('score must between 0~100')
            else:
                self._score=score
        else:
            raise ValueError('score must be intger!')


class Person(object):
    def __init__(self,name):
        self.name=name
   
    def __str__(self):
        return 'Person object(name:%s)' % self.name
