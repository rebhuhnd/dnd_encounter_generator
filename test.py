import unittest
from generator import Generator, d

class Test(unittest.TestCase):
    def test_n_encounters(self):
        generator = Generator()
        generator.load("encounters.csv")
        return

    def test_d(self):
        for x in range(0, 1000):
            roll = d("%")
            self.assertTrue(roll in xrange(0, 100),str(roll))

if __name__ == "__main__":
    unittest.main()
