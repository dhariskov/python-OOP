import unittest
from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("NewFact", 2)

    def test_add_ingredient_whenHaveSpaceAndCorrectIngredientBlue(self):
        self.paint_factory.add_ingredient("blue", 1)
        self.assertEqual(self.paint_factory.ingredients, {"blue": 1})
        self.paint_factory.add_ingredient("blue", 1)
        self.assertEqual(self.paint_factory.ingredients, {"blue": 2})

    def test_add_ingredient_whenDoNotHaveSpace(self):
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("blue", 4)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test_add_ingredient_whenIncorrectIngredient(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("Test", 1)
        self.assertEqual(str(ex.exception), "Ingredient of type Test not allowed in PaintFactory")

    def test_add_ingredient_whenIncorrectIngredientAndWrongAmount(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("Test", 100)
        self.assertEqual(str(ex.exception), "Ingredient of type Test not allowed in PaintFactory")

    def test_remove_ingredient_whenIngredientExistAndQuantityIsEnoughBlue(self):
        self.paint_factory.add_ingredient("blue", 2)
        self.paint_factory.remove_ingredient("blue", 1)
        self.assertEqual(self.paint_factory.ingredients, {"blue": 1})
        self.paint_factory.remove_ingredient("blue", 1)
        self.assertEqual(self.paint_factory.ingredients, {"blue": 0})

    def test_remove_ingredient_whenIngredientExistAndQuantityIsEnough(self):
        self.paint_factory.add_ingredient("blue", 2)
        self.paint_factory.remove_ingredient("blue", 1)
        self.assertEqual(self.paint_factory.ingredients, {"blue": 1})
        self.paint_factory.remove_ingredient("blue", 1)
        self.assertEqual(self.paint_factory.ingredients, {"blue": 0})

    def test_remove_ingredient_whenIngredientDoesNotExist(self):
        self.paint_factory.add_ingredient("blue", 2)
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("none", 3)
        self.assertEqual(str(ex.exception), "'No such ingredient in the factory'")

    def test_remove_ingredient_whenIngredientDoesNotExistAndQuantityOK(self):
        self.paint_factory.add_ingredient("blue", 2)
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("none", 3)
        self.assertEqual(str(ex.exception), "'No such ingredient in the factory'")

    def test_remove_ingredient_whenIngredientQuantityIncorrect(self):
        self.paint_factory.add_ingredient("blue", 2)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("blue", 3)
        self.assertEqual(str(ex.exception), "Ingredient quantity cannot be less than zero")


if __name__ == '__main__':
    unittest.main()
