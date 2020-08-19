import unittest

from project.survivor import Survivor


class TestSurvivor(unittest.TestCase):
    def setUp(self) -> None:
        self.survivor = Survivor("Test", 12)

    def test_setter_name(self):
        self.assertEqual(self.survivor.name, "Test")
        with self.assertRaises(ValueError) as ex:
            result = Survivor("", 12)
        self.assertEqual(str(ex.exception), "Name not valid!")

    def test_setter_age(self):
        self.assertEqual(self.survivor.age, 12)
        with self.assertRaises(ValueError) as ex:
            result = Survivor("Test", -1)
        self.assertEqual(str(ex.exception), "Age not valid!")

    def test_setter_health(self):
        self.assertEqual(self.survivor.health, 100)
        self.survivor.health = 1001
        self.assertEqual(self.survivor.health, 100)
        self.survivor.health = 10
        self.assertEqual(self.survivor.health, 10)
        with self.assertRaises(ValueError) as ex:
            self.survivor.health = -10
        self.assertEqual(str(ex.exception), "Health not valid!")

    def test_setter_needs(self):
        self.assertEqual(self.survivor.needs, 100)
        self.survivor.needs = 1001
        self.assertEqual(self.survivor.needs, 100)
        self.survivor.needs = 10
        self.assertEqual(self.survivor.needs, 10)
        with self.assertRaises(ValueError) as ex:
            self.survivor.needs = -10
        self.assertEqual(str(ex.exception), "Needs not valid!")

    def test_property_needs_sustenance(self):
        result = self.survivor.needs_sustenance
        self.assertEqual(result, False)
        self.survivor.needs -= 10
        result = self.survivor.needs_sustenance
        self.assertEqual(result, True)

    def test_property_needs_healing(self):
        result = self.survivor.needs_healing
        self.assertEqual(result, False)
        self.survivor.health -= 10
        result = self.survivor.needs_healing
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()

