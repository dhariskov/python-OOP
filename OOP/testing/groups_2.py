#Tested Code:
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + ' ' + self.surname

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __str__(self):
        people_str = ', '.join([str(person) for person in self.people])
        return "Group " + self.name + " with members " + people_str

    def __len__(self):
        return len(self.people)

    def __getitem__(self, index):
        return "Person " + str(index) + ": " + str(self.people[index])

    def __add__(self, other):
        return Group(self.name, self.people + other.people)

  #End tested code

import unittest


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.person1 = Person("Name1", "Surname1")
        self.person2 = Person("Name2", "Surname2")
        self.person3 = Person("Name1", "Surname2")

    def test_add(self):
        person = str(Person.__add__(self.person1, self.person2))
        self.assertEqual(person, "Name1 Surname2")

    def test_str(self):
        result = self.person1.__str__()
        self.assertEqual(result, "Name1 Surname1")


class TestGroup(unittest.TestCase):
    def setUp(self) -> None:
        self.people1 = Group("Gr_1", ["N1 F1", "N2 F2"])
        self.people2 = Group("Gr_2", ["N3 F3", "N4 F4"])

    def test_str(self):
        result = self.people1.__str__()
        self.assertEqual(result, "Group Gr_1 with members N1 F1, N2 F2")

    def test_len(self):
        result = self.people2.__len__()
        self.assertEqual(result, 2)

    def test_getitem(self):
        result = self.people1.__getitem__(0)
        self.assertEqual(result, "Person 0: N1 F1")

    def test_add(self):
        result = str(self.people1.__add__(self.people2))
        self.assertEqual(result, "Group Gr_1 with members N1 F1, N2 F2, N3 F3, N4 F4")




if __name__ == '__main__':
    unittest.main()
