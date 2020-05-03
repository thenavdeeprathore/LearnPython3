# global, class and local variables with the same names:

a, b = 100, 200  # global var


class Variables:
    a, b = 10, 20  # class var

    def add(self, a, b):  # local var
        print("Local: ", a + b)
        print("Instance: ", self.a + self.b)
        print("Global: ", globals()['a'] + globals()['b'])

    def mul(self, a, b):  # local var
        print("Local: ", a * b)
        print("Instance: ", self.a * self.b)
        print("Global: ", globals()['a'] * globals()['b'])


c = Variables()
c.add(1000, 2000)
c.mul(1000, 2000)
