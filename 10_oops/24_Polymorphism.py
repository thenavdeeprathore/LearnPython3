"""
Polymorphism:
------------
=>  poly means many. Morphs means forms.
=>  Polymorphism means 'Many Forms'.

Eg1: + operator acts as concatenation and arithmetic addition (operator overloading)
Eg2: * operator acts as multiplication and repetition operator
Eg3: The Same method with different implementations in Parent class and child classes. (overriding)

Related to Polymorphism the following 4 topics are important
1) Overloading
    1) Operator Overloading
    2) Method Overloading
    3) Constructor Overloading
2) Overriding
    1) Method Overriding
    2) Constructor Overriding
3) Pythonic behaviour
    1) DUck typing
    2) Easier to Ask Forgiveness than Permission (EAFP)
    3) Monkey patching
"""
# Operator overloading
print(10 + 20)
print("hello" + "world")


# method overriding
class P:

    def marry(self):
        print("Nicky")


class C(P):

    def marry(self):
        print("Sunny Leone")


c = C()
c.marry()  # Sunny Leone
