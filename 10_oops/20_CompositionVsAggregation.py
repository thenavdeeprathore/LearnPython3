"""
Has-A relation is also known as Composition and Aggregation
-----------------------------------------------------------

Composition {University --> Departments} ==> Strong object association
Aggregation {Departments --> Professor} ==> Weak object association

Conclusion:
The relation between object and its instance variables is always Composition
where as the relation between object and static variables is Aggregation
"""


class Student:

    college = "Harvard"

    def __init__(self, name):
        self.name = name


print(Student.college)  # Harvard
s = Student("Chris")
print(s.name)  # Chris


# In the above example without existing Student object there is no chance of existing his
# name. Hence Student Object and his name are strongly associated which is nothing but Composition.

# But without existing Student object there may be a chance of existing collegeName. Hence
# Student object and collegeName are weakly associated which is nothing but Aggregation.
