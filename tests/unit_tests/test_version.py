import unittest

import cbreakpoint as cb


class VersionTester(unittest.TestCase): 

#   def test_major(self):
#      self.assertEqual(cb.__version__[0], 0)
#
#   def test_minor(self):
#      self.assertEqual(cb.__version__[1], 1)
#
#   def test_last(self):
#      self.assertEqual(cb.__version__[2], 0)

   def test_condition_line(self):
      self.assertEqual(cb.condition_line(), 12)

   def test_with_argument(self):
      self.assertEqual(cb.cbreakpoint(21), 21)

   def test_with_keyword(self):
      self.assertEqual(cb.cbreakpoint(breakpoint_id=42), 42)

   def test_optional(self):
      self.assertEqual(cb.cbreakpoint(), -1)
