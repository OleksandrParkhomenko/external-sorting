import unittest
import os
from input_generation import *
from external_sorting import ExternalMergeSort


class TestInputFileGenerating(unittest.TestCase):

    def test_file_creation(self):
        file_size = 1000000
        delta = file_size // 100
        file = generate_input_file(file_size)
        self.assertAlmostEqual(file_size, os.path.getsize(file), None, "Create file with given size", delta)


class TestExternalMergeSort(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file_size = 10_000_000  # 10 mb
        cls.large_file = generate_input_file(cls.file_size)
        cls.sorting = ExternalMergeSort(cls.large_file, cls.file_size)

    def test_creating_tmp_folder(self):
        self.assertTrue(os.path.exists(self.sorting.dir), "Create tmp folder for storing chunks")

    def test_sort(self):
        def is_sorted(file_path):
            with open(file_path, 'r') as file:
                previous_line = file.readline()
                for line in file:
                    if line < previous_line:
                        return False
                    previous_line = line
            return True

        result_file = self.sorting.sort()
        self.assertTrue(is_sorted(result_file), "Result file is sorted")

