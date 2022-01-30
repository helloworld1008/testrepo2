#!/usr/bin/env python

import unittest
from src import MySum, MyProduct, MyDiff

class TestCode(unittest.TestCase):

	def test_mysum(self):

		self.assertEqual(MySum.mysum(5,4),9,"Must be 9")

	def test_myproduct(self):

		self.assertEqual(MyProduct.myproduct(9,9),81,"Must be 81")

	def test_mydiff(self):

		self.assertEqual(MyDiff.mydiff(18,9),9,"Must be 9")

if __name__ == "__main__":

	unittest.main()
