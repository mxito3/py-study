import random
class DataResolve:
    Result1,Result2,Result3=[],[],[]
    def resolve1(self):
        for i in range(10000):
            if i%3==0 and i%5!=0:
                self.Result1.append(i)
    def resolve2(self):
        self.resolve1()
        for i in self.Result1:
            if i%2==0:
                self.Result2+=self.Result1
        self.Result2.reverse()
        print("first resolve"+str(self.Result2))
    def resolve3(self):
        a=[random.randint(0,100) for _ in range(500)]
        print(set(a))
temp =DataResolve()
#temp.resolve2()
temp.resolve3()





