class Time:
    hour=0
    minute=0
    second=0
    def __str__(self):
        print(str("Time"))
    def test(self):
        self.__str__()
class Date:
    year=0
    month=0
    day=0
    # def __str__(self):
    #     print(str("Data"))
class DateTime(Time,Date):
    def __str__(self):
        super().__str__()
        print("DataTime")

    def test(self):
        super().test()

datetime=DateTime()
print(DateTime)
time=Time()
print(time.test())
# dt=DateTime()
# dt.__str__()
