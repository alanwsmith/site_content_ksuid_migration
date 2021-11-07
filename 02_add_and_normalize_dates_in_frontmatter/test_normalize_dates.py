#!/usr/bin/env python3

import difflib
import normalize_dates
import unittest
import filecmp
import sys
import io

class TestNormalizeDates(unittest.TestCase):

    def test_first_file(self):

        input_dir = "data_for_tests/input"
        output_dir = "data_for_tests/output"
        target_dir = "data_for_tests/targets"

        normalize_dates.make_files(
            input_dir=input_dir,
            output_dir=output_dir
        )

        file_list = ['1', '2', '3', '4']

        for file in file_list:
            a_file = f"{output_dir}/{file}.txt"
            b_file = f"{target_dir}/{file}.txt"
            with open(a_file) as _a:
                a_list = _a.read().splitlines()
            with open(b_file) as _b:
                b_list = _b.read().splitlines()
            self.assertListEqual(
                a_list, b_list
            )


if __name__ == "__main__":
    unittest.main()

