from day21 import Image, rotate
import unittest

class TestImage(unittest.TestCase):
    def setUp(self):
        self.image2 = Image(['.#', '..'])
        self.image3 = Image(['..#', '.#.', '#..'])
    
    def test_rotate(self):
        print(self.image2)
        self.assertEqual(
            rotate(self.image3.pattern),
            ['#..', '.#.', '..#']
        )
        self.assertEqual(
            rotate(self.image2.pattern),
            ['..', '.#']
        )

if __name__=='__main__':
    unittest.main()
