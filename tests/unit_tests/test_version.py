import unittest

import cbreakpoint as cb


class VersionTester(unittest.TestCase): 

   def test_major(self):
      self.assertEqual(cb.__version__[0], 0)

   def test_minor(self):
      self.assertEqual(cb.__version__[1], 1)

   def test_last(self):
      self.assertEqual(cb.__version__[2], 0)
