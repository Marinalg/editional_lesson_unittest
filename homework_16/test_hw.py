import unittest
import homework_zoo

class HomeWorkZooTest(unittest.TestCase):

    def negative_test(self):
        """print_total_of_category predators"""
        zoo = homework_zoo.Zoo()
        falcon = homework_zoo.Falcon("Falcon")
        parrots = homework_zoo.Parrots("Parrots")
        wolf = homework_zoo.Wolf("Wolf")
        zoo.add_animal(falcon)
        zoo.add_animal(parrots)
        zoo.add_animal(wolf)
        out = zoo.total_of_category("predators")
        exp = "8"
        self.assertEqual(out, exp)

    def test_b(self):
        self.assertEqual(homework_zoo.Wolf("1"))




if __name__ == "__main__":
    unittest.main(verbosity=2)