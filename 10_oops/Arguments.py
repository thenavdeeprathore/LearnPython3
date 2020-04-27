# default argument


class Test:

    def sum(self, a=None, b=None, c=None):
        print(a, b, c)


t = Test()
t.sum()  # None None None
t.sum(10, 20)  # 10 20 None
t.sum(10, 20, 30)  # 10 20 30


# variable length argument


class Test:

    def sum(self, *a):  # this *a will be represent as tuple
        count = 0
        for x in a:
            count = count + x
        print('Sum is: ', count)


t = Test()
t.sum(10, 20)  # Sum is:  30
t.sum(10, 20, 30)  # Sum is:  60
t.sum(10, 20, 30, 40)  # Sum is:  100



