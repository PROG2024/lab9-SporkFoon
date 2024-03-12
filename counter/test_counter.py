"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter

class TestCounterSingleton(unittest.TestCase):

    def setUp(self):
        Counter.reset()

    def test_singleton_instance_and_initial_count(self):
        counter1 = Counter()
        self.assertEqual(counter1.count, 1)
        counter1.count
        self.assertEqual(counter1.count, 1)

    def test_increment_and_shared_state(self):
      counter1 = Counter()
      
      counter1.increment()
      self.assertEqual(counter1.count, 2)

      counter2 = Counter()
      self.assertIs(counter1, counter2)
      self.assertEqual(counter2.count, 2)

      new_count = counter2.increment()
      self.assertEqual(new_count, 3)
      self.assertEqual(counter1.count, 3)


if __name__ == '__main__':
    unittest.main()
