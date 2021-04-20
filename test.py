import unittest
import os
from input_generation import *


class TestInputFileGenerating(unittest.TestCase):

    def test_file_creation(self):
        file_size = 1000000
        delta = file_size // 100
        file = generate_input_file(file_size)
        self.assertAlmostEqual(file_size, os.path.getsize(file), None, "Create file with given size", delta)
