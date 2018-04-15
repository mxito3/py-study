class Time:
    hour=0
    minute=0
    second=0
    def __str__(self):
        print(str("Time"))
    def test(self):
        self.__str__()
    def test1(self):
        print("in Time")
    def __init__(self):
        print("1")
class Date:
    year=0
    month=0
    day=0
    # def __str__(self):
    #     print(str("Data"))
    def test1(self):
        print("in Data")
class DateTime(Date,Time):
    # def __str__(self):
    #     super().__str__()
    #     print("DataTime")
     def test1(self):
         super(Date,self).test1()
         Time.test1(self)

datetime=DateTime()
datetime.test1()

